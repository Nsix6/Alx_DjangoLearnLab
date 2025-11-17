from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(name):
    return Book.objects.filter(author__name=name)

def books_in_library(library_name):
    return Library.objects.get(name=library_name).books.all()


def get_librarian_via_query(library):
    return library.librarian
