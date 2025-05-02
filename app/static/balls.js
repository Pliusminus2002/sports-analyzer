// Pasirenkame konteinerį, į kurį dėsim kamuolius
const container = document.querySelector('.falling-balls-container');

// Kelios kamuolių nuotraukos
const ballImages = [
  '/static/img/basketball.png',
  '/static/img/football.png',
  '/static/img/volleyball.png'
];

// Atsitiktinis skaičius tarp min ir max
function getRandom(min, max) {
  return Math.random() * (max - min) + min;
}

// Sukuriam vieną kamuolį
function createBall(imageSrc) {
  const ball = document.createElement('img');
  ball.src = imageSrc;
  ball.classList.add('falling-ball');
  ball.style.left = `${getRandom(0, window.innerWidth - 40)}px`;
  ball.style.animationDuration = `${getRandom(3, 7)}s`;

  // Ištrinam kai animacija baigiasi
  ball.addEventListener('animationend', () => {
    ball.remove();
  });

  container.appendChild(ball);
}

// Sukuriam 100 kamuolių
for (let i = 0; i < 100; i++) {
  const delay = getRandom(0, 3000); // atsitiktinis vėlavimas iki 3s
  setTimeout(() => {
    const img = ballImages[Math.floor(Math.random() * ballImages.length)];
    createBall(img);
  }, delay);
}
