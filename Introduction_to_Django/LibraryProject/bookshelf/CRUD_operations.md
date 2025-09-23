# CRUD_operations.md

Create:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

Retrieve:
```python
Book.objects.all()
Book.objects.get(id=1)
```

Update:
```python
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
```

Delete:
```python
book = Book.objects.get(id=1)
book.delete()
```
