from django.shortcuts import render, get_object_or_404
from .models import Book

def list_books(request):
    """View to list all books titles with their authors."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    """Library details, list all books"""
    model = Library
    context_object_name = 'library'
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs )
        context['books'] = self.object.books.all()
        return context
    

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("book_list")
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})
 


