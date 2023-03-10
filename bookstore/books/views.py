from django.views.generic import ListView, DeleteView

from .models import Book


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "book_list"


class BookDetailView(DeleteView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
