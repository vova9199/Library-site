from rest_framework import serializers, status


from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


# `http://127.0.0.1:8000/api/v1/users` - вывод всех юзеров
# `http://127.0.0.1:8000/api/v1/user/{id}?` - вывод конкретного юзера
# `http://127.0.0.1:8000/api/v1/user/{id}/orders?` - вывод всех orders конкретного юзера
# `http://127.0.0.1:8000/api/v1/user/{id}/order/{id}?` - вывод конкретного order конкретного юзера
# `http://127.0.0.1:8000/api/v1/order/{id}?` - вывод конкретного order, которые вернет и юзера, и книгу которую он взял
# `http://127.0.0.1:8000/api/v1/books` - вывод всех книг
# `http://127.0.0.1:8000/api/v1/book/{id}?` - вывод конкретной книги
# `http://127.0.0.1:8000/api/v1/authors - вывод всех автором
# `http://127.0.0.1:8000/api/v1/author/{id}?` - вывод конкретного автора

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'




class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    # authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        # fields = ['name', 'description', 'count', 'authors']
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
