from django.urls import path

from .views import Journals_reversedPageView, JournalsPageView, JournalDetailView

urlpatterns = [
    path('', JournalsPageView.as_view(), name='journals'),
    path('journals_reversed/', Journals_reversedPageView.as_view(), name='journals_reversed'),
    path('<int:pk>/', JournalDetailView.as_view(), name='detail_journal'),
]