document.addEventListener('DOMContentLoaded', () => {
    const cartTableBody = document.getElementById('cart-table-body');
    const subtotalElement = document.getElementById('subtotal');
    const taxElement = document.getElementById('tax');
    const discountElement = document.getElementById('discount');
    const finalTotalElement = document.getElementById('final-total');
    const promoCodeInput = document.getElementById('promo-code-input');
    const applyPromoButton = document.getElementById('apply-promo');

    let discount = 0;

    function updateTotals() {
        let subtotal = 0;

        cartTableBody.querySelectorAll('tr').forEach((row) => {
            const price = parseFloat(row.querySelector('.price').innerText.replace('$', ''));
            const quantity = parseInt(row.querySelector('input').value);
            const total = price * quantity;

            row.querySelector('.total').innerText = `$${total.toFixed(2)}`;
            subtotal += total;
        });

        const tax = subtotal * 0.10; // 10% tax
        const finalTotal = subtotal + tax - discount;

        subtotalElement.innerText = `$${subtotal.toFixed(2)}`;
        taxElement.innerText = `$${tax.toFixed(2)}`;
        discountElement.innerText = `$${discount.toFixed(2)}`;
        finalTotalElement.innerText = `$${finalTotal.toFixed(2)}`;
    }

    cartTableBody.addEventListener('click', (e) => {
        const button = e.target;
        if (button.classList.contains('increase') || button.classList.contains('decrease')) {
            const quantityInput = button.closest('.quantity').querySelector('input');
            let quantity = parseInt(quantityInput.value);

            if (button.classList.contains('increase')) quantity++;
            if (button.classList.contains('decrease') && quantity > 1) quantity--;

            quantityInput.value = quantity;
            updateTotals();
        }
    });

    applyPromoButton.addEventListener('click', () => {
        const promoCode = promoCodeInput.value.trim().toUpperCase();
        if (promoCode === 'DISCOUNT10') {
            discount = 10;
        } else {
            discount = 0;
        }
        updateTotals();
    });

    updateTotals();
});
