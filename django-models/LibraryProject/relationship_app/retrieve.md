# retrieve.md

Open Django shell:
```bash
python manage.py shell
```

Commands:
```python
from bookshelf.models import Book
# retrieve all books
books = Book.objects.all()
list(books.values())
# or retrieve the book with id=1
book = Book.objects.get(id=1)
book.title, book.author, book.publication_year
```

Expected output (example):
```
[{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]
# or
('1984', 'George Orwell', 1949)
```
