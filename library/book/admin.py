from author.admin import MembershipInline
from book.models import Book
from django.contrib import admin


class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def view_authors(obj):
        return "\n".join([author.surname for author in obj.authors.all()])

    inlines = [
        MembershipInline,
    ]

    list_display = ('id', 'name', 'description', 'count', 'view_authors')
    list_filter = ('id', 'name', 'authors')
    # fields = ('name', ('description', 'count'))
    fieldsets = (
        ('Information that does not change', {
            'fields': ('name', 'description',)
        }),
        ('Information that changes', {
            'fields': ('count',),
        }),
    )


admin.site.register(Book, BookAdmin)
