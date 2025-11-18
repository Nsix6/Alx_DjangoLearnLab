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
    

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView


class Register(CreateView):
    """User registration view"""
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


    def form_valid(self, form):
        user = form.save()
        print("Saved user:", user)
        return redirect('login')



