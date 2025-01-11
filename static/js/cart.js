// Get CSRF token from the cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if this cookie string begins with the name we want
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

document.getElementById('apply-promo').addEventListener('click', function() {
    const promoCode = document.getElementById('promo-code-input').value;

    if (promoCode.trim() === "") {
        alert("Please enter a promo code.");
        return;
    }

    fetch('/cart/apply-coupon/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Django CSRF token for security
        },
        body: JSON.stringify({ promo_code: promoCode })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);  // Show success or error message
        if (data.success) {
            window.location.reload();  // Reload the page to update the cart total
        }
    })
    .catch(error => console.error('Error:', error));
});

const carousel = document.querySelector('.carousel');
const nextBtn = document.querySelector('.next-btn');
const prevBtn = document.querySelector('.prev-btn');

let scrollPosition = 0;
const cardWidth = 240; // Card width + margin
const totalCards = document.querySelectorAll('.card').length;


nextBtn.addEventListener('click', () => {
    scrollPosition -= cardWidth;
    if (Math.abs(scrollPosition) >= cardWidth * (totalCards-4)) {
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

