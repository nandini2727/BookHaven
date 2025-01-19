from books.models import BrowsingHistory,Book
def get_browsing_history(request):
    if request.user.is_authenticated:
        history, created = BrowsingHistory.objects.get_or_create(user=request.user)
        return history.books.all()
    else:
        book_ids = request.session.get('browsing_history', [])
        return Book.objects.filter(id__in=book_ids)