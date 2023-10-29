from django.urls import path
from rest_framework.routers import SimpleRouter

from api import views
from api.views import CustomUserViewSet, OrderViewSet, BookViewSet, AuthorViewSet

# `http://127.0.0.1:8000/api/v1/users` - вывод всех юзеров
# `http://127.0.0.1:8000/api/v1/user/{id}?` - вывод конкретного юзера
# `http://127.0.0.1:8000/api/v1/user/{id}/orders?` - вывод всех orders конкретного юзера
# `http://127.0.0.1:8000/api/v1/user/{id}/order/{id}?` - вывод конкретного order конкретного юзера
# `http://127.0.0.1:8000/api/v1/order/{id}?` - вывод конкретного order, которые вернет и юзера, и книгу которую он взял
# `http://127.0.0.1:8000/api/v1/books` - вывод всех книг
# `http://127.0.0.1:8000/api/v1/book/{id}?` - вывод конкретной книги
# `http://127.0.0.1:8000/api/v1/authors - вывод всех автором
# `http://127.0.0.1:8000/api/v1/author/{id}?` - вывод конкретного автора

router = SimpleRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = router.urls

# urlpatterns += [
#     path('api/v1/user/<int:pk>/', views.CustomUserDetailView.as_view(), name='user-detail'),
#     # Add other URL patterns for your API endpoints here
# ]
