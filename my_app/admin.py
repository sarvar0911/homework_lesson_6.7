from django.contrib import admin

from my_app.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ...
