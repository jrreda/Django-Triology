from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)  # new
from django.views.generic import ListView, DeleteView

from .models import Book


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):  # new
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "book_list"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # new
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    permission_required = "books.special_status"
