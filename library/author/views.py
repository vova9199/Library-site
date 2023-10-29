from django.http import HttpResponseRedirect, request
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from authentication.models import CustomUser
from author.forms import AuthorCreateForm, AuthorEditForm
from author.models import Author
from django.views.generic import ListView
from abc import ABC


def author_id(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("login")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    return render(request, "get_author_by_id.html", context={"author": Author.get_by_id(id)})


class AbstractAuthorView(ABC):
    model = Author
    template_name = 'author.html'
    context_object_name = 'authors'
    paginate_by = 10

# class AuthorViewAll(AbstractAuthorView, ListView):
def get_all(request):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("login")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    return render(request, "author.html", {"author": Author.get_all()})


# def create_author(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         surname = request.POST['surname']
#         patronymic = request.POST['patronymic']
#         author = Author.create(name, surname, patronymic)
#         if author is None:
#             messages.error(request, "Something went wrong")
#
#         else:
#             messages.info(request, "Author created successfully")
#             return HttpResponseRedirect(reverse('all_author'))
#     else:
#         return render(request, 'author_form.html')

def create_author(request):
    if request.method == "POST":
        form = AuthorCreateForm(request.POST)
        if form.is_valid():
            author = form.save()
            messages.info(request, "Author created successfully")
            return redirect('all_author')
        else:
            messages.error(request, "Something went wrong")
    else:
        form = AuthorCreateForm()

    return render(request, 'author_form.html', {'form': form})

def edit_author(request, id):
    author = get_object_or_404(Author, pk=id)

    if request.method == "POST":
        form = AuthorEditForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.info(request, "Author edited successfully")
            return redirect('all_author')
        else:
            messages.error(request, "Something went wrong")
    else:
        form = AuthorEditForm(instance=author)

    return render(request, 'author_edit_form.html', {'form': form})

def delete_author(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("login")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    Author.delete_by_id(id)
    return redirect('all_author')

