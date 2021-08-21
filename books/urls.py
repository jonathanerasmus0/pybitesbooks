from django.urls import path

from books import views as book_views

app_name = 'books'
urlpatterns = [
    path('import_books', book_views.import_books, name='import_books'),
    path('<str:bookid>', book_views.book_page, name='book_page'),
]
