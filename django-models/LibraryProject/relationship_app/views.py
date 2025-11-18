from django.shortcuts import render, get_object_or_404
from relationship_app.models import Book, Library
from django.http import HttpResponse

def book_list(request):
    """View to list all books titles with their authors."""
    books = Book.objects.all()
    output = ""
    for book in books:
        output += f"{book.title} - {book.author.name}\n"

    return HttpResponse(output, content_type="text/plain")


from django.views.generic import DetailView

class BookListView(DetailView):
    """Library details, list all books"""
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs )
        context['books'] = self.object.books.all()
        return context

