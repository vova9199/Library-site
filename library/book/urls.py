from django.urls import path
import book.views as views
from order import views as order_views
from book import views as book_view


urlpatterns = [
    path("add_book/", views.create_book, name="add_book"),
    path('', views.all_books, name='books'),
    path('<str:param>', views.all_books, name='books_filtered'),
    path('confirm_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path("book_info/<int:id>/", views.book_info, name="book_info"),
    path("order_book/<int:id>/", order_views.order_book, name="order_book"),
    path("books_ordered/<int:id>/", views.books_ordered_by_user_id, name="books_ordered"),
    path("edit_book/<int:id>/", book_view.edit_book, name="edit_book"),
]
