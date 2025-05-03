from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, UserBook
from .forms import UserBookForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wishlist(request):
    books = Book.objects.all()
    return render(request, 'books/wishlist.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    userbook_form = UserBookForm()
    # userbook = UserBook.objects.filter(user=request.user, book=book).first()  # or use get() if guaranteed to exist

    return render(request, 'books/detail.html',{''
        'book' : book,
        'userbook_form' : userbook_form})

def mark_read(request, book_id):
    book = Book.objects.get(id=book_id)
    book.is_Read = True
    book.save()
    return render(request, 'books/detail.html', {'book': book})

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'is_Read']
    template_name = 'books/book_form.html'

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'genre', 'is_Read']
    template_name = 'books/book_form.html'

class BookDelete(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = '/wishlist/'
    
    