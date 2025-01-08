document.addEventListener('DOMContentLoaded', () => {
    const filters = {
        category: document.getElementById('category-filter'),
        price: document.getElementById('price-range'),
        sort: document.getElementById('sort-filter'),
        format: document.getElementById('format-filter'),
        ratings: document.querySelectorAll('.ratings input[type="checkbox"]'),
    };

    function applyFilters() {
        const selectedRatings = Array.from(filters.ratings)
            .filter(rating => rating.checked)
            .map(rating => rating.value);

        const params = new URLSearchParams({
            category: filters.category.value,
            price_max: filters.price.value,
            sort: filters.sort.value,
            format: filters.format.value,
        });

        selectedRatings.forEach(rating => params.append('ratings', rating));

        // Reload the page with new query parameters
        window.location.search = params.toString();
    }

    // Attach event listeners to all filter elements
    Object.values(filters).forEach(filter => {
        if (filter instanceof NodeList) {
            filter.forEach(item => item.addEventListener('change', applyFilters));
        } else {
            filter.addEventListener('change', applyFilters);
        }
    });
});