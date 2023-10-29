from django.urls import path
import order.views as views


urlpatterns = [
    path("order_book/", views.order_book, name="order_book"),
    path('all_orders/', views.all_orders, name='all_orders'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('close_order/<int:id>', views.close_order, name='close_order'),
    path('order/edit_order/<int:id>/', views.edit_order, name='edit_order'),
    path('close_order/<int:id>/', views.close_order, name='close_order'),

]
