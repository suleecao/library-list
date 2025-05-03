from django.shortcuts import render
from .models import Book

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wishlist(request):
    books = Book.objects.all()
    return render(request, 'books/wishlist.html', {'books': books})