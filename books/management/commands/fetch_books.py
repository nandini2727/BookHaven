import requests
from django.core.management.base import BaseCommand
from books.models import Book, Category
from django.conf import settings


class Command(BaseCommand):
    help = "Fetch books from Google Books API, adjust image URL zoom, download images, and save to database"

    def handle(self, *args, **kwargs):
        GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"
        API_KEY = settings.API_KEY
        categories = ["Aerospace Engineering", "Chemical Engineering","Biomedical Engineering","Robotics Engineering","Marine Engineering"]

        for category_name in categories:
            self.stdout.write(f"Fetching books for category: {category_name}")
            params = {
                "q": category_name,
                "printType": "books",
                "maxResults": 7,
                "key": API_KEY,
            }

            response = requests.get(GOOGLE_BOOKS_API_URL, params=params)

            if response.status_code == 200:
                books_data = response.json().get("items", [])
                category, created = Category.objects.get_or_create(name=category_name)

                for book_data in books_data:
                    volume_info = book_data.get("volumeInfo", {})
                    sale_info = book_data.get("saleInfo", {})
                    image_url = volume_info.get("imageLinks", {}).get("thumbnail", None)

                    if image_url:
                        # Append or update zoom=3
                        image_url = self.update_zoom_param(image_url)

                    try:
                        book, created = Book.objects.get_or_create(
                            title=volume_info.get("title", "Unknown Title"),
                            category=category,
                            defaults={
                                "author": ", ".join(volume_info.get("authors", [])),
                                "isbn": self.get_isbn(volume_info),
                                "description": volume_info.get("description", ""),
                                "price": sale_info.get("listPrice", {}).get("amount", 0.0),
                                "is_ebook": sale_info.get("isEbook", False),
                                "cover_image": image_url,
                                "popularity": volume_info.get("ratingsCount", 0),
                                "rating": volume_info.get("averageRating", 0.0),
                                "stock": 10,
                            },
                        )

                        if created:
                            self.stdout.write(f"Book added: {book.title}")
                        else:
                            self.stdout.write(f"Book already exists: {book.title}")

                    except Exception as e:
                        self.stderr.write(f"Error saving book: {e}")
            else:
                self.stderr.write(f"Failed to fetch books for category {category_name}. Status code: {response.status_code}")

    def update_zoom_param(self, url):
        """Helper function to add or update zoom=3 in the URL"""
        if "zoom=" in url:
            return url.replace("zoom=1", "zoom=3").replace("zoom=2", "zoom=3")
        return f"{url}&zoom=3" if "zoom=" not in url else url

    def get_isbn(self, volume_info):
        """Helper method to extract ISBN-13"""
        for identifier in volume_info.get("industryIdentifiers", []):
            if identifier.get("type") == "ISBN_13":
                return identifier.get("identifier")
        return None