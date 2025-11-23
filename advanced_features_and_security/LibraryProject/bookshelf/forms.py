from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """Secure Book form using Django validation (prevents SQL injection & unsafe input)."""
    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'publication_year']

    def clean_summary(self):
        summary = self.cleaned_data.get("summary", "")
        # Example sanitization (Task 5 requirement)
        return summary.strip()
