
removeButtons.forEach(button => {
    button.addEventListener('click', function () {
        const row = this.closest('tr');
        row.remove();
        updateProductCount();
    });
});

function updateProductCount() {
    const productCount = document.querySelectorAll('tbody tr').length;
    document.querySelector('p').innerText = `There are ${productCount} products in this wishlist.`;
}


