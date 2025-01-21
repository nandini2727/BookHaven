window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    const content = document.getElementById('content');
    const checkbox = document.getElementById('check');

    // After 4 seconds, check the checkbox
    setTimeout(() => {
      checkbox.checked = true; // Automatically check the checkbox

      // After 1 second of checking, show the content
      setTimeout(() => {
        preloader.style.display = 'none'; // Hide the preloader
        content.style.display = 'block'; // Show the main content
      }, 1000); 
    }, 2500); 
  });
  