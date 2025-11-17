# Started by typing the following in the python shell

book = Book.objects.create(
... title="1984",
... author="George Orwell",
... publication_year=1949
... )

book.save()

# the above creates an instance of Book, with given fields and saves to database
