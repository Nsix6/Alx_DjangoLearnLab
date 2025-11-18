from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Register
from django.views.generic import TemplateView


urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/page/', TemplateView.as_view(template_name='registration/logout_page.html'), name='logout_page'),
]