from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, UserBook
from .forms import UserBookForm

class HomeView(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

@login_required
def wishlist(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'books/wishlist.html', {'books': books})



STAR_CHOICES = [(i, f"{i} star{'s' if i != 1 else ''}") for i in range(6)]

@login_required
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
        "star_choices": STAR_CHOICES,
        "rating": book.rating
    })

@login_required
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
    
@login_required   
def add_finish_date(request, book_id):
    form = UserBookForm(request.POST)
    if form.is_valid():
        userbook = UserBook.objects.get(user=request.user, book_id=book_id)
        userbook.date = form.cleaned_data['date']
        userbook.recommend = form.cleaned_data['recommend']
        userbook.save()
        return redirect('book_detail', book_id=book_id)



class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'rating']
    template_name = 'books/book_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'genre', 'rating']
    template_name = 'books/book_form.html'
    # TODO: put calendar here instead of in book details

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = '/wishlist/'

    
    