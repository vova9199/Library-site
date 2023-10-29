import datetime

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from authentication.models import CustomUser
from book.models import Book
from order.models import Order
from django.core.checks import messages
from .forms import OrderCreateForm, OrderEditForm
from django.contrib import messages

def order_book(request, id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=id)

        if request.method == "POST":
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                messages.success(request, 'Ордер успішно створено!')
                return redirect('all_orders')  # або інший URL, куди ви хочете перенаправити користувача
            else:
                messages.error(request, 'Щось пішло не так. Будь ласка, спробуйте ще раз.')

        else:
            form = OrderCreateForm(initial={'book': book, 'user': request.user})

        return render(request, 'order_created.html', {'form': form})

    messages.error(request, 'Будь ласка, авторизуйтеся для створення ордера.')
    return redirect("login")

def edit_order(request, id):
    order = get_object_or_404(Order, pk=id)

    if request.method == "POST":
        form = OrderEditForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ордер успішно відредаговано!')
            return redirect('all_orders')
        else:
            messages.error(request, 'Щось пішло не так під час редагування. Будь ласка, спробуйте ще раз.')

    else:
        form = OrderEditForm(instance=order)

    return render(request, 'edit_order.html', {'form': form, 'order': order})

def close_order(request, id):
    if request.user.is_authenticated and request.user.role == 1:
        order = Order.objects.get(id=id)
        order.end_at = datetime.datetime.now()
        order.save()
        return redirect("all_orders")
    return redirect("home")


def all_orders(request):
    if request.user.is_authenticated and request.user.role == 1:
        orders = Order.objects.all()
        context = {
            'data': orders
        }
        return render(request, 'all_orders.html', context=context)
    return redirect("home")

def my_orders(request):
    if request.user.is_authenticated:
        print(request.user)
        user = CustomUser.objects.get(id=request.user.id)
        orders = Order.objects.filter(user=user)
        print(orders)
        context = {
            'data': orders
        }
        return render(request, 'my_orders.html', context=context)
    return redirect("home")
