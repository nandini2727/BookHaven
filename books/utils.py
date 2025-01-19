from .models import BrowsingHistory, Book

def track_browsing_history(request, book_id):
    book = Book.objects.get(id=book_id)

    # If the user is logged in, store browsing history in the database
    if request.user.is_authenticated:
        history, created = BrowsingHistory.objects.get_or_create(user=request.user)
        history.add_book(book)
    else:
        # For anonymous users, use the session
        if 'browsing_history' not in request.session:
            request.session['browsing_history'] = []

        browsing_history = request.session['browsing_history']

        # Avoid duplicates and limit to 15 items
        if book_id in browsing_history:
            browsing_history.remove(book_id)
        browsing_history.insert(0, book_id)

        # Keep only the last 15 items
        browsing_history = browsing_history[:15]

        # Save to session
        request.session['browsing_history'] = browsing_history
        request.session.modified = True
