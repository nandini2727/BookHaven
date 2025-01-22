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
    const selectedPayment = document.querySelector("input[name='payment_method']:checked");

    if (selectedAddress) {
        selectedAddressInput.value = selectedAddress.value;
    }

    if (selectedPayment) {
        paymentMethodInput.value = selectedPayment.value;
    }
});

// edit address Logic

document.addEventListener("DOMContentLoaded", () => {
  // Get references to form and elements
  const editLinks = document.querySelectorAll(".edit-address-link");
  const form = document.getElementById("deliveryForm");
  const submitButton = form.querySelector(".add-address-btn");

  // Function to populate the form with address data
  function populateFormWithAddress(link) {
      const addressId = link.dataset.id;

      // Populate form fields with address data
      document.getElementById("editAddressId").value = addressId;
      document.getElementById("name").value = link.dataset.name;
      document.getElementById("phone").value = link.dataset.phone;
      document.getElementById("email").value = link.dataset.email || "";
      document.getElementById("city").value = link.dataset.city;
      document.getElementById("state").value = link.dataset.state;
      document.getElementById("zip").value = link.dataset.zip;
      document.getElementById("address").value = link.dataset.address;

      // Update form button text
      submitButton.textContent = "Update Address";

      // Open the "Add a new address" accordion
      document.getElementById("third_acc").checked = true;
  }

  // Add event listeners to edit links
  editLinks.forEach((link) => {
      link.addEventListener("click", (e) => {
          e.preventDefault();
          populateFormWithAddress(link);
      });
  });

  // Reset form to "Add" mode on form submission
  form.addEventListener("submit", () => {
      submitButton.textContent = "Add Address";
  });
});

//set default address code
document.addEventListener("DOMContentLoaded", () => {
  // const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute("content");

  document.querySelectorAll(".set-default").forEach((p) => {
      p.addEventListener("click", function () {
          const addressId = this.dataset.addressId;

          fetch(`/set-default-address/${addressId}/`, {
              method: "POST",
              headers: {
                  "Content-Type": "application/json",
                  "X-CSRFToken": CSRF_TOKEN, // Use the CSRF token from the meta tag
              },
          })
              .then((response) => response.json())
              .then((data) => {
                  if (data.success) {
                      alert(data.message);
                      location.reload(); // Reload the page to reflect changes
                  } else {
                      alert(data.message);
                  }
              })
              .catch((error) => {
                  console.error("Error:", error);
                  alert("An error occurred. Please try again.");
              });
      });
  });
});
