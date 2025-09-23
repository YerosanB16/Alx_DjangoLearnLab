# create.md

Open Django shell:
```bash
python manage.py shell
```

Commands:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
```

Expected output (example):
```
<Book: 1984 by George Orwell>
```
