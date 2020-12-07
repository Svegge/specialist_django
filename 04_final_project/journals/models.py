from django.db import models
from django.urls import reverse

# Create your models here.
class Journal(models.Model):
    journal_name = models.CharField(max_length=250)
    journal_editor = models.CharField(max_length=100)
    journal_pages = models.IntegerField()

    def __str__(self):
        return self.journal_name + ' by ' + self.journal_editor
    
    def get_absolute_url(self):
        return reverse("detail_journal", args=[str(self.id)])