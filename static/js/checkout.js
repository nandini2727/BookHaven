document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', () => {
      const content = header.nextElementSibling;
  
      // Check if the current content is already open
      if (content.style.maxHeight) {
        content.style.maxHeight = null; // Close it
      } else {
        // Close all other sections
        document.querySelectorAll('.accordion-content').forEach(item => {
          item.style.maxHeight = null;
        });
  
        // Open the clicked section
        content.style.maxHeight = content.scrollHeight + 'px';
      }
    });
  });
document.addEventListener("DOMContentLoaded", function () {
    const addressRadios = document.querySelectorAll("input[name='address']");
    const paymentRadios = document.querySelectorAll("input[name='payment']");
    const selectedAddressInput = document.getElementById("selectedAddress");
    const paymentMethodInput = document.getElementById("paymentMethod");
    const checkoutForm = document.getElementById("checkoutForm");

    // Update selected address hidden input
    addressRadios.forEach(radio => {
        radio.addEventListener("change", function () {
            selectedAddressInput.value = this.value; // Use the ID of the selected address radio button
        });
    });

    // Update payment method hidden input
    paymentRadios.forEach(radio => {
        radio.addEventListener("change", function () {
            paymentMethodInput.value = this.value; // Use the value of the selected payment radio button
        });
    });

    // Set initial values for hidden inputs (default selections)
    const selectedAddress = document.querySelector("input[name='address']:checked");
    const selectedPayment = document.querySelector("input[name='payment']:checked");

    if (selectedAddress) {
        selectedAddressInput.value = selectedAddress.value;
    }

    if (selectedPayment) {
        paymentMethodInput.value = selectedPayment.value;
    }
    checkoutForm.addEventListener("submit", function (e) {
        
        console.log("Selected Address:", selectedAddressInput.value);
    });
});
