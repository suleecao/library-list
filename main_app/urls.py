from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/<int:book_id>/', views.book_detail, name='book_detail'),
    # path('wishlist/create/', views.BookCreate.as_view(), name='book-create'),
    path('wishlist/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('wishlist/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path('wishlist/<int:book_id>/add_userbook/', views.add_userbook, name='add_userbook'),
    path('wishlist/<int:book_id>/add-finish-date/', views.add_userbook, name='add_finish_date'),

]
