# updates the instance title

book = Book.objects.get(title="1984")
book.title = 'Nineteen Eighty-Four'

> > > new_book.save()

# first line updates the title values and then saves to memeory
