const container = document.querySelector('.falling-balls-container');
const ballTypes = ['basketball', 'football', 'volleyball'];
const totalBalls = 100;

for (let i = 0; i < totalBalls; i++) {
  const img = document.createElement('img');
  const type = ballTypes[Math.floor(Math.random() * ballTypes.length)];
  img.src = `/static/img/${type}.png`;
  img.style.left = Math.random() * 100 + 'vw';
  img.style.top = '-50px';
  img.style.animation = `fall ${5 + Math.random() * 5}s linear ${Math.random() * 5}s infinite`;
  container.appendChild(img);
}

// Animate falling with CSS
const style = document.createElement('style');
style.innerHTML = `
  @keyframes fall {
    to {
      transform: translateY(120vh) rotate(360deg);
      opacity: 0;
    }
  }
`;
document.head.appendChild(style);
