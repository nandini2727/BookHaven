const booksContainer = document.getElementById('books-container');
const formatFilter = document.getElementById('format-filter');
const categoryFilter = document.getElementById('category-filter');
const priceRange = document.getElementById('price-range');
const priceRangeValue = document.getElementById('price-range-value');
const sortFilter = document.getElementById('sort-filter');
const prevBtn = document.getElementById('prev-btn');
const nextBtn = document.getElementById('next-btn');
const pageInfo = document.getElementById('page-info');

// Example books data
const books = [
    { id: 1, title: 'Civil Engineering Basics', price: 30, format: 'ebook', category: 'civil', popularity: 4, image: 'https://via.placeholder.com/150' },
    { id: 2, title: 'Python for Beginners', price: 25, format: 'ebook', category: 'computer', popularity: 5, image: 'https://via.placeholder.com/150' },
    { id: 3, title: 'Mechanical Wonders', price: 40, format: 'hardcopy', category: 'mechanical', popularity: 3, image: 'https://via.placeholder.com/150' },
    { id: 4, title: 'Electricity Demystified', price: 35, format: 'hardcopy', category: 'electrical', popularity: 4, image: 'https://via.placeholder.com/150' },
    { id: 5, title: 'Advanced Programming', price: 50, format: 'ebook', category: 'computer', popularity: 5, image: 'https://via.placeholder.com/150' },
    { id: 6, title: 'Construction Strategies', price: 60, format: 'hardcopy', category: 'civil', popularity: 2, image: 'https://via.placeholder.com/150' },
    { id: 7, title: 'Electrical Engineering Insights', price: 45, format: 'ebook', category: 'electrical', popularity: 4, image: 'https://via.placeholder.com/150' },
    { id: 8, title: 'Introduction to Mechanical Systems', price: 55, format: 'hardcopy', category: 'mechanical', popularity: 3, image: 'https://via.placeholder.com/150' },
    { id: 9, title: 'Civil Engineering Basics', price: 30, format: 'ebook', category: 'civil', popularity: 4, image: 'https://via.placeholder.com/150' },
    { id: 10, title: 'Python for Beginners', price: 25, format: 'ebook', category: 'computer', popularity: 5, image: 'https://via.placeholder.com/150' },
    { id: 11, title: 'Mechanical Wonders', price: 40, format: 'hardcopy', category: 'mechanical', popularity: 3, image: 'https://via.placeholder.com/150' },
    { id: 12, title: 'Electricity Demystified', price: 35, format: 'hardcopy', category: 'electrical', popularity: 4, image: 'https://via.placeholder.com/150' },
    { id: 13, title: 'Advanced Programming', price: 50, format: 'ebook', category: 'computer', popularity: 5, image: 'https://via.placeholder.com/150' },
    { id: 14, title: 'Construction Strategies', price: 60, format: 'hardcopy', category: 'civil', popularity: 2, image: 'https://via.placeholder.com/150' },
    { id: 15, title: 'Electrical Engineering Insights', price: 45, format: 'ebook', category: 'electrical', popularity: 4, image: 'https://via.placeholder.com/150' },
    { id: 16, title: 'Introduction to Mechanical Systems', price: 55, format: 'hardcopy', category: 'mechanical', popularity: 3, image: 'https://via.placeholder.com/150' },
    // Add more books as needed
];

let currentPage = 1;
const itemsPerPage = 9;

function displayBooks() {
    const start = (currentPage - 1) * itemsPerPage;
    const end = start + itemsPerPage;

    // Clear current books
    booksContainer.innerHTML = '';

    // Display paginated books
    const filteredBooks = applyFilters();
    const paginatedBooks = filteredBooks.slice(start, end);

    paginatedBooks.forEach(book => {
        const bookCard = document.createElement('div');
        bookCard.className = 'book-card';
        bookCard.innerHTML = `
            <img src="${book.image}" alt="${book.title}">
            <h3>${book.title}</h3>
            <p>$${book.price}</p>
            <button class="add-to-cart">Add to Cart</button>
            <button class="buy-now">Buy Now</button>
        `;
        booksContainer.appendChild(bookCard);
    });

    pageInfo.textContent = `Page ${currentPage}`;
}

function applyFilters() {
    const format = formatFilter.value;
    const category = categoryFilter.value;
    const maxPrice = parseInt(priceRange.value);
    const sort = sortFilter.value;

    let filteredBooks = books.filter(book => {
        return (format === 'all' || book.format === format) &&
            (category === 'all' || book.category === category) &&
            book.price <= maxPrice;
    });

    if (sort === 'price-low') {
        filteredBooks.sort((a, b) => a.price - b.price);
    } else if (sort === 'price-high') {
        filteredBooks.sort((a, b) => b.price - a.price);
    } else if (sort === 'popularity') {
        filteredBooks.sort((a, b) => b.popularity - a.popularity);
    } else if (sort === 'newest') {
        filteredBooks.sort((a, b) => b.id - a.id); // Assuming newer books have higher IDs
    }

    return filteredBooks;
}

priceRange.addEventListener('input', () => {
    priceRangeValue.textContent = `$0 - $${priceRange.value}`;
    displayBooks();
});

formatFilter.addEventListener('change', displayBooks);
categoryFilter.addEventListener('change', displayBooks);
sortFilter.addEventListener('change', displayBooks);

prevBtn.addEventListener('click', () => {
    if (currentPage > 1) {
        currentPage--;
        displayBooks();
    }
});

nextBtn.addEventListener('click', () => {
    const totalPages = Math.ceil(applyFilters().length / itemsPerPage);
    if (currentPage < totalPages) {
        currentPage++;
        displayBooks();
    }
});

// Initial display
displayBooks();