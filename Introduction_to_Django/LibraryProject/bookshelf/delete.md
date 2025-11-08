# deletes instance of Book created

book = Book.objects.get(title="1984")
book.delete()
(1, {'bookshelf.Book': 1})

# command on line 3/4, deletes the instance and line 5 hows the feedback
