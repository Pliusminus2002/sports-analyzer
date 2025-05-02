// Pasirenkame konteinerį, į kurį dėsim kamuolius
const container = document.querySelector('.falling-balls-container');

// Kelių tipų kamuolių nuotraukos (keliami iš /static/img/)
const ballImages = [
  '/static/img/basketball.png',
  '/static/img/football.png',
  '/static/img/volleyball.png'
];

// Funkcija atsitiktinei reikšmei tarp min ir max
function getRandom(min, max) {
  return Math.random() * (max - min) + min;
}

// Funkcija sukurti vieną kamuolį
function createBall(imageSrc) {
  const ball = document.createElement('img');
  ball.src = imageSrc;
  ball.classList.add('falling-ball');
  
  // Stiliai, padedantys atsitiktinai išmesti kamuolį
  ball.style.position = 'absolute';
  ball.style.top = `-${getRandom(50, 150)}px`;
  ball.style.left = `${getRandom(0, window.innerWidth - 50)}px`;
  ball.style.width = `${getRandom(20, 50)}px`;
  ball.style.opacity = 0.9;

  // Animacijos greitis ir kryptis
  ball.style.animationDuration = `${getRandom(3, 7)}s`;
  ball.style.animationDelay = `${getRandom(0, 2)}s`;

  // Įdedame į puslapį
  container.appendChild(ball);

  // Pašalinam po 10 sekundžių (kai jau nukrito)
  setTimeout(() => {
    container.removeChild(ball);
  }, 10000);
}

// Sukuriame ~100 kamuolių atsitiktinai iš visų rūšių
for (let i = 0; i < 100; i++) {
  const randomImg = ballImages[Math.floor(Math.random() * ballImages.length)];
  createBall(randomImg);
}
