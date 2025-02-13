document.addEventListener("DOMContentLoaded", function () {
    const messages = [
        "Тикни",
        "Ще раз тикни",
        "Ну ще трошки",
        "Оооо, ось воно!",
        "Люблю тебе ❤️"
    ];

    let currentMessageIndex = 0;
    const messageElement = document.querySelector(".message");

    document.addEventListener("click", function () {
        if (currentMessageIndex < messages.length - 1) {
            currentMessageIndex++;
            messageElement.textContent = messages[currentMessageIndex];
        }
    });

    // Додаємо ефект сердечок
    function createHeart() {
        const heart = document.createElement("div");
        heart.classList.add("heart");
        heart.innerHTML = "❤️";
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.fontSize = Math.random() * 20 + 20 + "px";
        document.body.appendChild(heart);

        setTimeout(() => {
            heart.remove();
        }, 4000);
    }

    setInterval(createHeart, 300);
    document.body.addEventListener("click", createHeart);

    // Інтеграція з Telegram WebApp
    const tg = window.Telegram.WebApp;
    tg.expand(); // Розширюємо WebApp на весь екран
});