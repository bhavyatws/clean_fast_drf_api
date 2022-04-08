from django.urls import path
from api import views

urlpatterns = [
    path('userlist/', views.UserList.as_view(),name="userlist"),
    path('books/', views.BookListCreateAPIView.as_view(), name="book_list")
]