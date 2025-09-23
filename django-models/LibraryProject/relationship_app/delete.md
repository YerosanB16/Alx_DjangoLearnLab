# delete.md

Open Django shell:
```bash
python manage.py shell
```

Commands:
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
# confirm deletion
Book.objects.filter(id=1).exists()
```

Expected output (example):
```
False
```
