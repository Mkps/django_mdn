from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = \
            ('first_name', 'last_name', 'date_of_birth', 'date_of_death')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = \
            ('title', 'author', 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre)
admin.site.register(Language)
