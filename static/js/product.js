
function showTab(tabId) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(content => {
      content.classList.remove('active');
    });
  
    // Remove active class from all buttons
    const tabButtons = document.querySelectorAll('.tab-button');
    tabButtons.forEach(button => {
      button.classList.remove('active');
    });
  
    // Show the selected tab content
    const selectedTab = document.getElementById(tabId);
    if (selectedTab) {
      selectedTab.classList.add('active');
    }
  
    // Set the clicked tab button as active
    const activeButton = document.querySelector(`.tab-button[onclick="showTab('${tabId}')"]`);
    if (activeButton) {
      activeButton.classList.add('active');
    }
  }
// Weight selection
const weightButtons = document.querySelectorAll('.weight-btn');
weightButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove active class from all buttons
        weightButtons.forEach(btn => btn.classList.remove('active'));
        // Add active class to clicked button
        button.classList.add('active');
    });
});

// Quantity selector
const decreaseBtn = document.querySelector('.decrease');
const increaseBtn = document.querySelector('.increase');
const qtyInput = document.querySelector('.qty-input');

decreaseBtn.addEventListener('click', () => {
    let qty = parseInt(qtyInput.value);
    if (qty > 1) {
        qtyInput.value = qty - 1;
    }
});

increaseBtn.addEventListener('click', () => {
    let qty = parseInt(qtyInput.value);
    if(qty>4)
      increaseBtn.disabled=true
    else
      qtyInput.value = qty + 1;
});


