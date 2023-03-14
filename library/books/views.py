from django.views.generic import ListView

from .models import Book


# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "book_list"
