from django.contrib import admin
from .models import Series, Author, Book, Search, Upload

admin.site.register(Author)
admin.site.register(Series)
admin.site.register(Book)
admin.site.register(Search)
admin.site.register(Upload)