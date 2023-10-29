from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
from .serializers import CustomUserSerializer, OrderSerializer, BookSerializer, AuthorSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=False, methods=['delete'])
    def custom_user_delete(self, request):
        user_id = request.data.get('id')  # Предположим, что вы отправляете ID пользователя для удаления в поле 'id'
        user = CustomUser.get_by_id(user_id)

        if not user:
            return Response({'detail': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

        # Вы можете добавить дополнительные проверки (например, проверку на роль или права доступа) здесь

        # Удаление пользователя
        user.delete()

        return Response({'detail': 'Пользователь успешно удален'}, status=status.HTTP_204_NO_CONTENT)

class CustomUserDetailView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def create(self, request, *args, **kwargs):
    #     # Check if 'author' is provided in the request data
    #     if 'author' not in request.data:
    #         return Response({"author": ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     # Retrieve the author ID from the request data
    #     author_id = request.data.pop('author')
    #
    #     # Check if the author with the provided ID exists
    #     author = Author.get_by_id(author_id)
    #     if author is None:
    #         return Response({"author": ["Author does not exist."]}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     # Create the book, including the author
    #     serializer = BookSerializer(data=request.data)
    #     if serializer.is_valid():
    #         book = serializer.save()
    #         book.authors.add(author)  # Add the author to the book
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
