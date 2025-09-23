# update.md

Open Django shell:
```bash
python manage.py shell
```

Commands:
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
# confirm update
Book.objects.get(id=1).title
```

Expected output (example):
```
'Nineteen Eighty-Four'
# or printed as
Nineteen Eighty-Four
```
