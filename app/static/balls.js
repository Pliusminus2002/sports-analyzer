document.addEventListener("DOMContentLoaded", function () {
    const images = [
        "/static/img/basketball.png",
        "/static/img/football.png",
        "/static/img/volleyball.png"
    ];

    for (let i = 0; i < 150; i++) {
        const img = document.createElement("img");
        img.src = images[Math.floor(Math.random() * images.length)];
        img.className = "ball";
        img.style.left = `${Math.random() * 100}vw`;
        img.style.top = `-${Math.random() * 200}px`;
        img.style.animationDuration = `${2 + Math.random() * 4}s`;
        img.style.zIndex = 0;
        document.body.appendChild(img);
    }
});
