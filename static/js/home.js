const carousel = document.querySelector('.carousel');
const nextBtn = document.querySelector('.next-btn');
const prevBtn = document.querySelector('.prev-btn');

let scrollPosition = 0;
const cardWidth = 220; // Card width + margin
const totalCards = document.querySelectorAll('.card').length;


nextBtn.addEventListener('click', () => {
    scrollPosition -= cardWidth;
    if (Math.abs(scrollPosition) >= cardWidth * (totalCards-3)) {
        scrollPosition = 0; // Reset to the start
    }
    carousel.style.transform = `translateX(${scrollPosition}px)`;
});
prevBtn.addEventListener('click', () => {
    scrollPosition += cardWidth;
    if (scrollPosition > 0) {
        scrollPosition = -(cardWidth * (totalCards - 4)); // Go to the last card
    }
    carousel.style.transform = `translateX(${scrollPosition}px)`;
});


document.addEventListener("DOMContentLoaded", () => {
    const categoryItems = document.querySelectorAll(".newArr-category li");
    const imageDisplay = document.getElementById("newArr-category-img");

    categoryItems.forEach(item => {
        item.addEventListener("mouseover", () => {
            const imageName = item.getAttribute("data-image");
            imageDisplay.src = imageName;
        });
    });
});


document.querySelectorAll('.newArr-list li').forEach(item => {
    item.addEventListener('mouseover', function() {
        // Get the description from the data attribute
        const description = this.getAttribute('data-description');

        // Update the description text
        document.getElementById('image-description').textContent = description;
    });

});

