document.addEventListener("DOMContentLoaded", function () {
    const messages = [
        "Тикни",
        "Ще раз тикни",
        "Ну ще трошки",
        "Оооо, ось воно!",
        "Люблю тебе ❤️",
        "Ти найкращий(а) 😊",
        "Обіймаю тебе 🤗",
        "Моє серденько твоє ❤️",
        "Разом назавжди 💞",
        "Ти мій всесвіт 🌍",
        "Просто знай: я тебе люблю 🥰"
    ];

    let currentMessageIndex = 0;
    const messageElement = document.querySelector(".message");

    document.addEventListener("click", function () {
        if (currentMessageIndex < messages.length - 1) {
            currentMessageIndex++;
            messageElement.textContent = messages[currentMessageIndex];
        } else {
            // Коли досягли останнього тексту - додаємо велике сердечко
            showBigHeart();
        }
    });

    function showBigHeart() {
        // Перевіряємо, чи сердечко вже є, щоб не додавати повторно
        if (!document.querySelector(".big-heart")) {
            const heart = document.createElement("div");
            heart.classList.add("big-heart");
            heart.innerHTML = "❤️";
            document.body.appendChild(heart);
        }
    }

    // Додаємо ефект маленьких сердечок
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

    const tg = window.Telegram.WebApp;
    tg.expand(); 
});