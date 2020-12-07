from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Journal

class JournalsPageView(ListView):
    model = Journal
    template_name = 'journals.html'
    context_object_name = 'journals'

class JournalDetailView(DetailView):
    model = Journal
    template_name = 'detail_journal.html'
    context_object_name = 'journal'

class Journals_reversedPageView(ListView):
    model = Journal
    template_name = 'journals_reversed.html'
    context_object_name = 'journals_reversed'
    ordering = ['-journal_pages']

class JournalCreateView(CreateView):
    model = Journal
    template_name = 'new_journal.html'
    fields = ('journal_name', 'journal_editor', 'journal_pages')
    