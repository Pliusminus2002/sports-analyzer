const ballImages = [
  "{{ url_for('static', filename='img/krepšinio.png') }}",
  "{{ url_for('static', filename='img/futbolo.jpg') }}",
  "{{ url_for('static', filename='img/Tinklinio.jpg') }}"
];

function createBall() {
  const ball = document.createElement("div");
  ball.classList.add("ball");
  ball.style.left = Math.random() * window.innerWidth + "px";
  ball.style.animationDuration = 4 + Math.random() * 4 + "s";
  ball.style.backgroundImage = `url(${ballImages[Math.floor(Math.random() * ballImages.length)]})`;
  document.body.appendChild(ball);

  setTimeout(() => {
    ball.remove();
  }, 9000);
}

setInterval(createBall, 150);
