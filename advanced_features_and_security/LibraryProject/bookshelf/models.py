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



from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user manager to handle user creation.
    """
    class Meta:
        permission = [
            ('can_view', 'Can view content'),
            ('can_edit', 'Can edit content'),
            ('can_delete', 'Can delete content'),
            ('can_create', 'Can create content'),
        ]
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        
        return self.create_user(username, email, password, **extra_fields)



class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django AbstractUser.
    Additional fields can be added here as needed.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()


    def __str__(self):
        return self.username

