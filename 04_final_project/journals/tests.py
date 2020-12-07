from django.test import TestCase
from .models import Journal

# Create your tests here.
class JournalModelTest(TestCase):
    '''
    Тест валидности модели Journal
    '''
    def setUp(self):
        '''
        Добавление тестового объекта в модель Book
        '''
        Journal.objects.create(journal_name='test_journal_name', journal_editor = 'test_journal_editor', journal_pages = int('1'))

    def test_book_creation(self):
        '''
        Проверка корректности создания объекта в модели Journal
        '''
        current_journal = Journal.objects.values_list('journal_name', flat=True)[0]
        current_editor = Journal.objects.values_list('journal_editor', flat=True)[0]
        current_pages = int(Journal.objects.values_list('journal_pages', flat=True)[0])        
        expected_journal_name = 'test_journal_name'
        expected_journal_editor = 'test_journal_editor'
        expected_journal_pages = int('1')

        self.assertEqual(current_journal, expected_journal_name)
        self.assertEqual(current_editor, expected_journal_editor)
        self.assertEqual(current_pages, expected_journal_pages)

class JournalsUrlTest(TestCase):
    def test_journals_page_url(self):
        response = self.client.get('/journals/')
        self.assertEqual(response.status_code, 200)

class JournalsReversedUrlTest(TestCase):
    def test_journals_reversed_page_url(self):
        response = self.client.get('/journals/journals_reversed/')
        self.assertEqual(response.status_code, 200)

class JournalsDetailedUrlTest(TestCase):
    def test_journals_reversed_page_url(self):
        response = self.client.get('/journals/1/')
        self.assertEqual(response.status_code, 200)