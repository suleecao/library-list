from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
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
    userbook = None
    if request.user.is_authenticated:
        try:
            userbook = UserBook.objects.get(user=request.user, book=book)
        except UserBook.DoesNotExist:
            pass  
    star_choices = [(i, '★' * i) for i in range(1, 6)]
    userbook_form = UserBookForm(instance=userbook) 

    context = {
        'book': book,
        'star_choices': star_choices,
        'userbook': userbook,
        'userbook_form': userbook_form,
    }
    return render(request, 'books/detail.html', context)

@login_required
class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'rating']
    template_name = 'books/book_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def add_userbook(request, book_id):
    form = UserBookForm(request.POST)
    book = Book.objects.get(id=book_id)
    if form.is_valid():
        userbook, created = UserBook.objects.get_or_create(
            user=request.user,
            book=book,
            defaults={'date': form.cleaned_data.get('date')}
        )
        if not created:
            userbook.date = form.cleaned_data.get('date')
            userbook.save()
        return redirect('book_detail', book_id=book.id)
    else:
        return render(request, 'books/detail.html', {'book': book, 'userbook_form': form})
    
@login_required   
def add_finish_date(request, book_id):
    form = UserBookForm(request.POST)
    if form.is_valid():
        try:
            userbook = UserBook.objects.get(user=request.user, book_id=book_id)
            userbook.date = form.cleaned_data['date']
            userbook.recommend = form.cleaned_data['recommend']
            userbook.save()
            messages.success(request, 'Finish date updated successfully!')
            return redirect('book_detail', book_id=book_id)
        except UserBook.DoesNotExist:
            messages.error(request, 'User book not found.')
            return render(request, 'books/detail.html', {'form': form, 'userbook_form': form})
    else:
        return render(request, 'books/detail.html', {'form': form, 'error_msg': 'Invalid form submission.'})
    

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

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = '/wishlist/'

    
    