from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import Book

class HomePageView(TemplateView):
    template_name='home.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'new_book.html'
    fields = ('book_name', 'book_author', 'book_rating')

class BooksPageView(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'detail_book.html'
    context_object_name = 'book'

class Books_reversedPageView(ListView):
    model = Book
    template_name = 'books_reversed.html'
    context_object_name = 'books_reversed'

    ordering = ['-book_rating']