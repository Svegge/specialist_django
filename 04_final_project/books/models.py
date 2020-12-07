from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=250)
    book_author = models.CharField(max_length=200)
    book_rating = models.IntegerField()

    def __str__(self):
        return self.book_author + ': ' + self.book_name
    
    def get_absolute_url(self):
        return reverse("detail_book", args=[str(self.id)])