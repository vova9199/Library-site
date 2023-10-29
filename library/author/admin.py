from django.contrib import admin
from author.models import Author


class MembershipInline(admin.TabularInline):
    model = Author.books.through
    extra = 1


class AuthorAdmin(admin.ModelAdmin):

    inlines = [
        MembershipInline,
    ]
    exclude = ('books',)

    @staticmethod
    def view_books(obj):
        return "\n".join([book.name for book in obj.books.all()])

    list_display = ('id', 'name', 'surname', 'patronymic', 'view_books')
    list_filter = ('id', 'name', 'books')
    fields = ('name', ('surname', 'patronymic'))


admin.site.register(Author, AuthorAdmin)
