from django.urls import path
from . import views
from .views import HomePageView

urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('borrows/', views.BorrowRecordListView.as_view(), name='borrow-list'),

    path('authors/add/', views.AuthorCreateView.as_view(), name='add-author'),
    path('books/add/', views.BookCreateView.as_view(), name='add-book'),
    path('borrows/add/', views.BorrowRecordCreateView.as_view(), name='add-borrow'),

    path('export/', views.export_to_excel, name='export-excel'),
]
