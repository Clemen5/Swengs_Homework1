from django.contrib import admin

from .models import Author, Book, Publisher
from . import models


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre')
    list_filter = ("authors__last_name",)
    pass


admin.site.register(Book, BookAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    pass


admin.site.register(Publisher, PublisherAdmin)

