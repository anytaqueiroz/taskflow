from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///taskflow.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    status = db.Column(db.String(20), default='todo')  # todo, doing, done
    priority = db.Column(db.String(10), default='media')  # baixa, media, alta
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'created_at': self.created_at.strftime('%d/%m/%Y')
        }
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = {
        'todo':  Task.query.filter_by(status='todo').all(),
        'doing': Task.query.filter_by(status='doing').all(),
        'done':  Task.query.filter_by(status='done').all(),
    }
    return render_template('index.html', tasks=tasks)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User(
            name=name,
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()

        print("USUÁRIO CADASTRADO:")
        print(name)
        print(email)

        return redirect(url_for('index'))

    return render_template('register.html')
@app.route('/task', methods=['POST'])
def create_task():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    priority = request.form.get('priority', 'media')
    if priority not in ('baixa', 'media', 'alta'):
        priority = 'media'
    if title:
        db.session.add(Task(title=title, description=description, priority=priority))
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/task/<int:task_id>/status', methods=['POST'])
def update_status(task_id):
    task = Task.query.get_or_404(task_id)
    new_status = request.form.get('status')
    if new_status in ('todo', 'doing', 'done'):
        task.status = new_status
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/users')
def users():

    usuarios = User.query.all()

    resultado = "<h1>Usuários Cadastrados</h1>"

    for usuario in usuarios:
        resultado += f"""
        <p>
        ID: {usuario.id}<br>
        Nome: {usuario.name}<br>
        Email: {usuario.email}
        </p>
        <hr>
        """

    return resultado
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('FLASK_DEBUG', 'false').lower() == 'true')
