function openModal() {
  document.getElementById('modal').classList.add('active');
  setTimeout(() => document.querySelector('.modal input[name="title"]').focus(), 50);
}

function closeModal(e) {
  if (!e || e.target.id === 'modal' || e.target.classList.contains('btn-cancel')) {
    document.getElementById('modal').classList.remove('active');
  }
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
});
