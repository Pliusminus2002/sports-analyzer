// Paimam konteinerį
const container = document.querySelector('.falling-balls-container');

// Jinja sugeneruoja tikrą URL šitam JS faile kaip globalius kintamuosius
const ballImages = window.ballImages || [];

// Random funkcija
function getRandom(min, max) {
  return Math.random() * (max - min) + min;
}

// Kamuolio kūrimas
function createBall(imageSrc) {
  const ball = document.createElement('img');
  ball.src = imageSrc;
  ball.classList.add('falling-ball');
  ball.style.left = `${getRandom(0, 100)}vw`;
  ball.style.width = `${getRandom(20, 40)}px`;
  ball.style.animationDuration = `${getRandom(3, 6)}s`;
  ball.style.zIndex = '1';
  container.appendChild(ball);

  setTimeout(() => {
    ball.remove();
  }, 7000);
}

// Sukuriam ~300 kamuolių atsitiktinai
for (let i = 0; i < 300; i++) {
  const delay = getRandom(0, 5000);
  setTimeout(() => {
    const img = ballImages[Math.floor(Math.random() * ballImages.length)];
    createBall(img);
  }, delay);
}
