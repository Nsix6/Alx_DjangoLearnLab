from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', views.list_books, name='book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    path('login/', LoginView.as_view(
        template_name="relationship_app/login.html"
    ), name='login'),

    path('register/', views.register, name='register'),

    path('logout/', LogoutView.as_view(
        template_name="relationship_app/logout.html"
    ), name='logout'),

    path("admin-page/", views.admin_view, name="admin_view"),
    path("librarian-page/", views.librarian_view, name="librarian_view"),
    path("member-page/", views.member_view, name="member_view"),

    path('book/add_book/', views.add_book, name='add_book'),
    path('book/<int:pk>/edit_book/', views.edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
]
