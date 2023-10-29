import datetime
from itertools import count

from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
from .forms import BookForm, BookEditForm
from django.contrib import messages


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST or None)
        authors = Author.objects.all()
        if form.is_valid():
            # Створюємо книгу, але не зберігаємо її в базу даних
            book = form.save(commit=False)

            # Зберігаємо книгу в базу даних
            book.save()

            # Додаємо авторів до книги
            for author in form.cleaned_data['authors']:
                book.authors.add(author)

            return redirect('books')  # замініть на URL, на який ви хочете перейти після успішного створення книги
    else:
        form = BookForm()

    context = {'form': form}
    return render(request, 'book_create.html', context)

def edit_book(request, id):
    book = Book.objects.get(pk=id)

    if request.method == "POST":
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.info(request, "Book edited successfully")
            return redirect('books')
        else:
            messages.error(request, "Something went wrong")
    else:
        form = BookEditForm(instance=book)

    return render(request, 'book_edit.html', {'form': form})



def all_books(request):
    if request.user.is_authenticated:
        raw_books = Book.objects.all()
        data = []
        for book in raw_books:
            print(book.authors.all())
            authors = ', '.join([f'{author.name} {author.surname}' for author in book.authors.all()])
            print(authors)
            data.append({'id': book.id,
                         'name': book.name,
                         'description': book.description,
                         'authors': authors,
                         'count': book.count})
        context = {
            'data': data
        }
        return render(request, 'books.html', context=context)
    return redirect("login")


def book_info(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)
        authors = ', '.join([f'{author.name} {author.surname}' for author in book.authors.all()])
        available = book.count - Order.objects.filter(book=book, end_at=None).count()
        context = {'id': book.id,
                   'name': book.name,
                   'description': book.description,
                   'authors': authors,
                   'count': book.count,
                   'available': available}
        return render(request, 'book_info.html', context=context)
    return redirect("login")


def books_ordered_by_user_id(request, id):
    if request.user.is_authenticated and request.user.role == 1:
        if user := CustomUser.get_by_id(id):
            orders = Order.objects.filter(user=user, end_at=None)
            print(orders)
            return render(request, 'books_ordered.html', {'data': orders})
        else:
            messages.error(request, 'ERROR! No user found')
    return redirect("books")

def book_delete(request, book_id):
    # Get the book object to delete
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST' and 'action' in request.POST:
        action = request.POST['action']
        if action == 'delete':
            book.delete()

            return redirect('books')

    context = {
        'book': book,
    }
    return render(request, 'book_delete.html', context)

def filter_books():
    return None