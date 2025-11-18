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