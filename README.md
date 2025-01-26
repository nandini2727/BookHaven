# BookHaven

Welcome to **BookHaven**, your one-stop platform for buying engineering books in both e-book and hardcopy formats. Built with Django, this website provides a seamless user experience for exploring, purchasing, and managing books. Whether you're a student, professional, or educator, BookHaven is tailored to meet your needs.

---

## Features

### User Management

- **User Authentication**: Secure login, signup, and logout functionalities.
- **Profile Management**: Update user details and manage saved addresses.

### Product Browsing

- **Book Categories**: Browse books by engineering disciplines.
- **Search and Filter**: Quickly find books using the search bar or filters.
- **Book Details**: View detailed descriptions, prices, and formats for each book.

### Cart and Checkout

- **Add to Cart**: Add books to your cart in desired quantities.
- **Address Selection**: Choose a delivery address or add a new one during checkout.
- **Order Summary**: Review your cart items and total price before placing an order.

### Order Management

- **Order History**: View past orders with details like books purchased, address used, and order status.
- **Track Orders**: Monitor the progress of your orders.

### Recommendations

- **Personalized Suggestions**: Get recommendations based on the books in your cart.

---

## Installation

### Prerequisites

- Python 3.8+
- Django 4.x
- A database system (SQLite, PostgreSQL, etc.)
- Virtual Environment (optional but recommended)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/bookhaven.git
   cd bookhaven
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:

   - Open `bookhaven/settings.py` and update the `DATABASES` setting for your preferred database.

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Visit the application at `http://127.0.0.1:8000/`.

---

## Project Structure

```plaintext
bookhaven/
├── bookhaven/         # Core project settings and configuration
├── books/             # App for managing book-related features
├── cart/              # App for managing cart and checkout functionality
├── orders/            # App for handling order creation and history
├── users/             # App for user authentication and profile management
├── templates/         # HTML templates
├── static/            # Static files (CSS, JS, images)
├── media/             # Media files (e.g., book covers)
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## Key Models

### `Book`

- `title`
- `author`
- `price`
- `format` (e-book or hardcopy)
- `description`
- `category`

### `Cart`

- `user`
- Related `CartItems`

### `Order`

- `user`
- `items` (relation to books)
- `address`
- `status`
- `created_at`

---

## Usage

1. **Add Books**:
   - As an admin, log in to the Django admin panel (`/admin`) and add books.
2. **Explore Books**:
   - Visit the homepage to browse available books.
3. **Purchase Books**:
   - Add books to the cart, choose an address, and proceed with checkout.
4. **View Orders**:
   - Check the "Order History" section to track your orders.

---

## Future Enhancements

- **Reviews and Ratings**: Allow users to review and rate books.
- **Discounts and Offers**: Add promotional campaigns for users.
- **REST API**: Provide API support for third-party integrations.

---

## Contributing

We welcome contributions to improve BookHaven! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Submit a pull request.

---

Happy Reading with **BookHaven**!

