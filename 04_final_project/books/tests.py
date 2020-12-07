from django.test import TestCase
from .models import Book

# Create your tests here.
class BookModelTest(TestCase):
    '''
    Тест валидности модели Books
    '''
    def setUp(self):
        '''
        Добавление тестового объекта в модель Book
        '''
        Book.objects.create(book_name='test_book_name', book_author = 'test_book_author', book_rating = int('1'))

    def test_book_creation(self):
        '''
        Проверка корректности создания объекта в модели Book
        '''
        current_book = Book.objects.values_list('book_name', flat=True)[0]
        current_author = Book.objects.values_list('book_author', flat=True)[0]
        current_rating = int(Book.objects.values_list('book_rating', flat=True)[0])        
        expected_book_name = 'test_book_name'
        expected_book_author = 'test_book_author'
        expected_book_rating = int('1')

        self.assertEqual(current_book, expected_book_name)
        self.assertEqual(current_author, expected_book_author)
        self.assertEqual(current_rating, expected_book_rating)

class BooksUrlTest(TestCase):
    def test_books_page_url(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

class BooksReversedUrlTest(TestCase):
    def test_books_reversed_page_url(self):
        response = self.client.get('/books/books_reversed/')
        self.assertEqual(response.status_code, 200)

class BooksDetailedUrlTest(TestCase):
    def test_books_reversed_page_url(self):
        response = self.client.get('/books/1/')
        self.assertEqual(response.status_code, 200)

class BooksHomeUrlTest(TestCase):
    def test_books_home_page_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)