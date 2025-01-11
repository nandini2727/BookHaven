from books.models import Book
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_books(cart):
    # Fetch all books
    books = Book.objects.all()

    # Fetch books currently in the cart
    cart_books = cart.items.values_list('book__id', flat=True)

    # Convert books into a pandas DataFrame
    books_df = pd.DataFrame.from_records(books.values(
        'id', 'title', 'description', 'category__name', 'popularity', 'rating'
    ))

    # Combine relevant features into a single column for similarity
    books_df['combined_features'] = (
        books_df['title'] + ' ' +
        books_df['description'] + ' ' +
        books_df['category__name']
    )

    # Initialize TF-IDF Vectorizer
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(books_df['combined_features'])

    # Calculate cosine similarity between all books
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Get indices of books in the cart
    cart_indices = books_df[books_df['id'].isin(cart_books)].index

    # Aggregate similarity scores for books in the cart
    similarity_scores = similarity_matrix[cart_indices].sum(axis=0)

    # Add similarity scores to the DataFrame
    books_df['similarity_score'] = similarity_scores

    # Exclude books already in the cart
    recommended_books = books_df[~books_df['id'].isin(cart_books)]

    # Sort by similarity, then by popularity and rating
    recommended_books = recommended_books.sort_values(
        by=['similarity_score', 'popularity', 'rating'], ascending=False
    )[:9]  # Limit to top 5 recommendations

    # Fetch Book objects for the recommendations
    recommended_book_ids = recommended_books['id'].tolist()
    return Book.objects.filter(id__in=recommended_book_ids)
