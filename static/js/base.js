const userIcon = document.getElementById('user-icon');
        const userDialog = document.getElementById('user-dialog');

        userIcon.addEventListener('click', () => {
            if (userDialog.style.display === 'none' || userDialog.style.display === '') {
                userDialog.style.display = 'block';
            } else {
                userDialog.style.display = 'none';
            }
        });

        // Close the dialog when clicking outside of it
        document.addEventListener('click', (event) => {
            if (!userIcon.contains(event.target) && !userDialog.contains(event.target)) {
                userDialog.style.display = 'none';
            }
        });