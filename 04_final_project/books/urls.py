from django.urls import path

from .views import HomePageView, BooksPageView, Books_reversedPageView, BookDetailView, BookCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('books/', BooksPageView.as_view(), name='books'),
    path('books/books_reversed/', Books_reversedPageView.as_view(), name='books_reversed'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='detail_book'),
    path('books/new/', BookCreateView.as_view(), name='new_book'),
]