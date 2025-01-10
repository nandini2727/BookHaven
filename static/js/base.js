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


        
const searchIcon = document.getElementById("searchIcon");
const searchBox = document.querySelector(".searchBox");
searchIcon.addEventListener("click", function () {
if (searchIcon.classList.contains("fa-magnifying-glass")) {
    searchIcon.classList.remove("fa-magnifying-glass", "searchBtn");
    searchIcon.classList.add("fa-xmark", "closeBtn");
} else {
        searchIcon.classList.remove("fa-xmark", "closeBtn");
        searchIcon.classList.add("fa-magnifying-glass", "searchBtn");
    }
});
document.addEventListener("DOMContentLoaded", function() {
    

    console.log(searchIcon); // Should log the icon element
    console.log(searchBox); // Should log the search box element

    if (searchIcon && searchBox) {
        searchIcon.addEventListener("click", function() {
            searchBox.classList.toggle("active");
        });
    } else {
        console.error("Search icon or search box not found!");
    }
});
document.addEventListener('click', (event) => {
    if (!searchIcon.contains(event.target) && !searchBox.contains(event.target)) {
        searchBox.classList.remove("active");
        searchIcon.classList.remove("fa-xmark", "closeBtn");
        searchIcon.classList.add("fa-magnifying-glass", "searchBtn");
    }
});