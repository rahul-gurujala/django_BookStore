from django.shortcuts import get_object_or_404, render
from django.http import Http404
from book_outlet.models import Book
from django.db.models import Avg

# Create your views here.


def index(request):
    books = Book.objects.all().order_by('-rating')
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'num_books': books.count(),
        'avg_rating': books.aggregate(Avg('rating'))
    })


def book_detail(request, slug):
    # try: book = Book.objects.get(pk=_id)
    # except: raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestselling
    })
