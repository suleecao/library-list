from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/<int:book_id>/', views.book_detail, name='book_detail'),
    path('wishlist/<int:book_id>/mark_read/', views.mark_read, name='mark_read'),
]
#     path('books/', views.book_list, name='book_list'),
#     path('books/<int:book_id>/', views.book_detail, name='book_detail'),
#     path('authors/', views.author_list, name='author_list'),
#     path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
