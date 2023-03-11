from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)  # new
from django.db.models import Q  # new
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


class SearchResultsListView(ListView):  # new
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
