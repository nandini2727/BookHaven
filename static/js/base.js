const userIcon = document.getElementById('user-icon');
const userDialog = document.getElementById('user-dialog');
const subMenuWrap = document.querySelector('.sub-menu-wrap');

userIcon.addEventListener('click', (event) => {
    event.stopPropagation(); // Prevent the click event from bubbling up
    subMenuWrap.classList.toggle('open');
});


document.addEventListener('click', (event) => {
    if (!subMenuWrap.contains(event.target) && !userIcon.contains(event.target)) {
        subMenuWrap.classList.remove('open');
    }
});
const svg = document.querySelector('.searchBox i');
const input = document.querySelector('.input');

svg.addEventListener('click', () => {
  input.focus(); 
});   
// const searchIcon = document.getElementById("searchIcon");
// const searchBox = document.querySelector(".searchBox");
// searchIcon.addEventListener("click", function () {
// if (searchIcon.classList.contains("fa-magnifying-glass")) {
//     searchIcon.classList.remove("fa-magnifying-glass", "searchBtn");
//     searchIcon.classList.add("fa-xmark", "closeBtn");
// } else {
//         searchIcon.classList.remove("fa-xmark", "closeBtn");
//         searchIcon.classList.add("fa-magnifying-glass", "searchBtn");
//     }
// });
// document.addEventListener("DOMContentLoaded", function() {

//     if (searchIcon && searchBox) {
//         searchIcon.addEventListener("click", function() {
//             searchBox.classList.toggle("activate");
//         });
//     } else {
//         console.error("Search icon or search box not found!");
//     }
// });
// document.addEventListener('click', (event) => {
//     if (!searchIcon.contains(event.target) && !searchBox.contains(event.target)) {
//         searchBox.classList.remove("activate");
//         searchIcon.classList.remove("fa-xmark", "closeBtn");
//         searchIcon.classList.add("fa-magnifying-glass", "searchBtn");
//     }
// });