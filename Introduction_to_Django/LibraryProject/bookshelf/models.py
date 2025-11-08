from django.db import models

# Create your models here.

class Book(models.Model):
    """
    Defines a Book model with title, author, and publication year fields.
    """
    title  = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        """
        Docstring for __str__
        
        :param self: Description
        """
        return f"{self.title} by {self.author} ({self.publication_year})"
