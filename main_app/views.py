from django.shortcuts import get_object_or_404, redirect, render
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

# STAR_CHOICES = [(i, f"{i} star{'s' if i != 1 else ''}") for i in range(6)]

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        new_rating = int(request.POST.get("rating", 0))
        new_rating = max(0, min(5, new_rating))
        book.rating = new_rating
        book.save()
        return redirect(request.path)

    return render(request, "books/detail.html", {
        "book": book,
        # "star_choices": STAR_CHOICES,
    })


def add_userbook(request, book_id):
    form = UserBookForm(request.POST)
    book = Book.objects.get(id=book_id)
    if form.is_valid():
        userbook, created = UserBook.objects.get_or_create(
            user=request.user,
            book=book,
            defaults={'finish_date': form.cleaned_data.get('finish_date')}
        )
        
        if not created:
            userbook.finish_date = form.cleaned_data.get('finish_date')
            userbook.save()
        return redirect('book_detail', book_id=book.id)
    else:
        return render(request, 'books/detail.html', {'book': book, 'userbook_form': form})

# def add_userbook(request, book_id):
#     form = UserBookForm(request.POST)
#     book = Book.objects.get(id=book_id)
#     if form.is_valid():
#         userbook = form.save(commit=False)
#         userbook.user = request.user
#         userbook.book = book
#         userbook.save()
#         return redirect(request, 'books/detail.html', {'userbook': userbook})
#     else:
#         return render(request, 'books/detail.html', {'book': book})

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'rating']
    template_name = 'books/book_form.html'

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'genre', 'rating']
    template_name = 'books/book_form.html'

class BookDelete(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = '/wishlist/'

    
    