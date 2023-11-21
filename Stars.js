const numStars = 100; // Количество звезд

for (let i = 0; i < numStars; i++) {
  const star = document.createElement('div');
  star.className = 'star';
  
  // Генерируем случайные координаты для каждой звезды
  const top = Math.random() * 100;
  const left = Math.random() * 100;

  star.style.top = top + '%';
  star.style.left = left + '%';

  document.body.appendChild(star);
}

// Анимация мерцания звезд
setInterval(() => {
    const stars = document.querySelectorAll('.star'); // Получаем все элементы звезд
  
    stars.forEach((star) => {
      star.style.animation = 'twinkling 1s infinite'; // Устанавливаем анимацию мерцания для каждой звезды
    });
  }, 500);