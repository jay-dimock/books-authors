from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addbook', views.addbook),
    path('authors', views.authors),
    path('addauthor', views.addauthor),
    path('book/<int:id>', views.book),
    path('author/<int:id>', views.author),
    path('add-book-to-author', views.addBookToAuthor),
    path('add-author-to-book', views.addAuthorToBook),
]