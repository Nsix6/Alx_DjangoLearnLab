# Simple retrieveal of books in the session database

book = Book.objects.get(title="1984")
<QuerySet [<Book: 1984 by George Orwell (1949)>]>

# line 3,is the command to save and line 4 gives the outcome
