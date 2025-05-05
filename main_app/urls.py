from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/<int:book_id>/', views.book_detail, name='book_detail'),
    # path('wishlist/<int:book_id>/mark_read/', views.mark_read, name='mark_read'),
    path('wishlist/create/', views.BookCreate.as_view(), name='book-create'),
    path('wishlist/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('wishlist/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path('wishlist/<int:book_id>/add_userbook/', views.add_userbook, name='add_userbook'),

]
