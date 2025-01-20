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
setInterval(()=>{
    scrollPosition -= cardWidth;
    if (Math.abs(scrollPosition) >= cardWidth * (totalCards-3)) {
        scrollPosition = 0; // Reset to the start
    }
    carousel.style.transform = `translateX(${scrollPosition}px)`;

},4000)

document.addEventListener("DOMContentLoaded", () => {
    const categoryItems = document.querySelectorAll(".newArr-category li");
    const imageDisplay = document.getElementById("newArr-category-img");
    const booklink=document.getElementById("newArr-category-link")

    categoryItems.forEach(item => {
        item.addEventListener("mouseover", () => {
            const imageName = item.getAttribute("data-image");
            const bookName=item.getAttribute("data-book");
            imageDisplay.src = imageName;
            booklink.href=`/product/${bookName}/`;
            categoryItems.forEach((el)=>el.classList.remove("active"))
            item.classList.add("active");
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

document.addEventListener("DOMContentLoaded", () => {
    const sliderTrack = document.querySelector('.slider-track');
  
    // Clone the slider track and append it
    const clonedTrack = sliderTrack.cloneNode(true);
    sliderTrack.parentNode.appendChild(clonedTrack);
  
    // Adjust the width of the parent container
    const totalWidth = sliderTrack.offsetWidth * 2;
    const parentContainer = sliderTrack.parentNode;
    parentContainer.style.display = "flex";
    // parentContainer.style.width = `${totalWidth}px`;
  });

  document.addEventListener("DOMContentLoaded", function () {
    const textElements = document.querySelectorAll(".text h1");
    let currentText = 0;

    // Function to show the current text and hide others
    function showText(index) {
        textElements.forEach((text, i) => {
            if (i === index) {
                text.classList.add("active"); // Show the current text
            } else {
                text.classList.remove("active"); // Hide other texts
            }
        });
    }

    // Automatically transition texts every 3 seconds
    setInterval(() => {
        currentText = (currentText + 1) % textElements.length; // Move to the next text
        showText(currentText); // Show the new text
    }, 4000);

    // Show the first text initially
    showText(currentText);
});

document.addEventListener("DOMContentLoaded", function () {
    const slider = document.querySelector(".slider");
    const slides = document.querySelectorAll(".slider img");
    const dots = document.querySelectorAll(".slider-nav a");

    const totalSlides = slides.length;
    let currentSlide = 0;

    function showNextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides; // Move to the next slide
        const scrollAmount = slides[currentSlide].offsetLeft; // Calculate scroll position
        slider.scrollTo({ left: scrollAmount, behavior: "smooth" }); // Scroll to the next slide

        // Update active dot
        dots.forEach((dot, index) => {
            dot.style.opacity = index === currentSlide ? 1 : 0.75;
        });
    }
    setInterval(showNextSlide, 4000);
});