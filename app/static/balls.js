document.addEventListener('DOMContentLoaded', () => {
  const body = document.body;
  const ballImages = [
    "{{ url_for('static', filename='img/basketball.png') }}",
    "{{ url_for('static', filename='img/football.png') }}",
    "{{ url_for('static', filename='img/volleyball.png') }}"
  ];

  for (let i = 0; i < 100; i++) {
    const img = document.createElement('img');
    img.src = ballImages[Math.floor(Math.random() * ballImages.length)];
    img.classList.add('falling-ball');
    img.style.left = Math.random() * 100 + 'vw';
    img.style.animationDuration = (2 + Math.random() * 4) + 's';
    img.style.animationDelay = (Math.random() * 3) + 's';
    img.style.width = '30px';
    img.style.position = 'absolute';
    body.appendChild(img);
  }
});
