from django.db import models
from django.urls import reverse 
from django.db.models import UniqueConstraint 

# Create your models here.

class Book(models.Model):
    """
    Defines a Book model with title, author, and publication year fields.
    """
    title  = models.CharField(max_length=200, unique=True, help_text="Title of the book")
    author = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True, max_length=1000, help_text="Brief summary of the book",)
    publication_year = models.IntegerField()

    class Meta:
        """
        Meta class for Book model to define constraints.
        """
        constraints = [
            UniqueConstraint(fields=['title'], name='unique_book_title', violation_error_message="A book with this title already exists.")
        ]

    def __str__(self):
        """
        Docstring for __str__
        
        :param self: Description
        """
        return f"{self.title} by {self.author} ({self.publication_year})"
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])
