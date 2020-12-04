from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from .models import Book

class HomePageView(TemplateView):
    template_name='home.html'

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