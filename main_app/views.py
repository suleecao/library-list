from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Book

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wishlist(request):
    books = Book.objects.all()
    return render(request, 'books/wishlist.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})

def mark_read(request, book_id):
    book = Book.objects.get(id=book_id)
    book.is_Read = True
    book.save()
    return render(request, 'books/detail.html', {'book': book})

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'is_Read']
    template_name = 'books/book_form.html'
    
    