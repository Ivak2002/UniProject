document.addEventListener('DOMContentLoaded', () => {
  const userMenu = document.getElementById('userMenu');
  const userMenuContent = document.getElementById('userMenuContent');

  if (!userMenu || !userMenuContent) return;


  userMenu.querySelector('i').addEventListener('click', (e) => {
    e.stopPropagation();
    userMenuContent.classList.toggle('show');
  });


  document.addEventListener('click', () => {
    userMenuContent.classList.remove('show');
  });


  userMenuContent.addEventListener('click', (e) => {
    e.stopPropagation();
  });
});