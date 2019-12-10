from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('new/book', views.new_book, name='new_book'),
    path('add/author/<int:num>', views.add_author, name='add_author'),
    path('authors', views.authors, name='authors'),
    path('authors/<int:num>', views.author_info, name="author_info"),
    path('new/author', views.new_author, name='new_author'),
    path('add/book<int:num>', views.add_book, name='add_book'),
    path('book/info/<int:num>', views.book_info, name='book_info'),
    path('author/info/<int:id>', views.author_info, name='author_info'),
]