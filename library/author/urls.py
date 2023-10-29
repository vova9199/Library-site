from django.urls import path
import author.views as views
# from .views import AuthorViewAll


urlpatterns = [
    path("create/", views.create_author, name="create_author"),
    path("edit/<int:id>/", views.edit_author, name="edit_author"),
    path('<int:id>/', views.author_id, name='author_by_id_url'),
    # path('', AuthorViewAll.as_view(), name='all_author'),
    path('', views.get_all, name='all_author'),
    path("delete/<int:id>/", views.delete_author, name="delete_author"),

    ]