from django.urls import path
from books_app import views

app_name = 'books_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('read/<int:pk>/', views.read_book, name='read_book'),
]