from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate

from .forms import CustomUserCreationForm, CustomLoginForm, CustomUserUpdateForm
from .models import CustomUser
from django.contrib import messages, auth


# def register(request):
#     redirect_authenticated_user = True
#
#     if request.method == 'POST':
#         data = request.POST
#         user = CustomUser.objects.create_user(email=data['email'],
#                                               password=data['password'],
#                                               first_name=data['name'],
#                                               middle_name=data['middle_name'],
#                                               last_name=data['last_name'],
#                                               role=data['role'],
#                                               )
#         user.save()
#         if user:
#             return redirect('home')
#
#     form = [{'id_name': 'name', 'name': 'First Name'},
#             {'id_name': 'middle_name', 'name': 'Middle name'},
#             {'id_name': 'last_name', 'name': 'Last name'},
#             {'id_name': 'email', 'name': 'Email'},
#             {'id_name': 'password', 'name': 'Password'},
#             {'id_name': 'role', 'name': 'Role'}
#             ]
#     context = {
#         'form': form
#     }
#     return render(request, 'register.html', context=context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if 'submit_action' in request.POST:
            submit_action = request.POST['submit_action']
            if submit_action == 'Register':
                if form.is_valid():
                    user = form.save()
                    # Log in the user
                    if user is not None:
                        auth.login(request=request, user=user)
                        user.is_active = True
                        user.save()
                    messages.success(request, 'Registration successful!')
                    return redirect('home')  # Redirect to the user's profile or another page
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


# def login(request):
#     if request.method != 'POST':
#         return render(request, 'login.html')
#     user = CustomUser.get_by_email(
#         email=request.POST['emailAddress']
#     )
#
#     if user:
#         if not user.check_password(request.POST['password']):
#             messages.error(request, 'ERROR! Incorrect password!')
#             return redirect("login")
#     else:
#         messages.error(request, 'ERROR! The user does not exist, please sign up!')
#         return redirect("login")
#
#     auth.login(request=request, user=user)
#     user.is_active = True
#     user.save()
#     messages.success(request, 'Success! You are logged in!')
#
#     return redirect("home")

def login(request):
    if request.method == 'POST':
        user = CustomUser.get_by_email(
                email=request.POST['email']
            )

        if user:
            if user.password == request.POST['password']:
                auth.login(request=request, user=user)
                user.is_active = True
                user.save()
                messages.success(request, 'Success! You are logged in!')
                return redirect("home")
            else:
                messages.error(request, 'ERROR! Incorrect password!')
                return redirect("login")
        else:
            messages.error(request, 'ERROR! The user does not exist, please sign up!')
            return redirect("login")

    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    messages.info(request, "Logged out!")
    return redirect("home")


def get_all(request):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("login")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    return render(request, "get_users.html", {"users": CustomUser.get_all()})


def user_info(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("login")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    return render(request, "get_user_by_id.html", context={"user": CustomUser.get_by_id(id)})


def edit_user_info(request, id):
    user = get_object_or_404(CustomUser, id=id)

    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('get_users')  # Redirect to the user's profile page after editing
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, 'edit_user_profile.html', {'form': form})

def delete_user(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("login")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    CustomUser.delete_by_id(id)
    messages.success(request, 'User has been deleted successfully!')
    return redirect("get_users")


def home(request):
    return render(request, "home.html")
