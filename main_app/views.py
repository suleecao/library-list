from django.shortcuts import render
from django.http import HttpResponse

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

books = [
    Book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
    Book("1984", "George Orwell", "Dystopian"),         
    Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic"),
    Book("Vineland", "Thomas Pynchon", "Modernist"),
    Book("The Catcher in the Rye", "J.D. Salinger", "Fiction"),
    Book("Brave New World", "Aldous Huxley", "Dystopian"),
    Book("  The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    Book("The Lord of the Rings", "J.R.R. Tolkien", "Fantasy"),
    Book("Pride and Prejudice", "Jane Austen", "Romance"),
    Book("The Diary of Anne Frank", "Anne Frank", "Biography"),
]

def home(request):
    return HttpResponse("<h1>Welcome to the Library List App!</h1>")

def about(request):
    return render(request, 'about.html')

def wishlist(request):
    return render(request, 'books/wishlist.html', {'books': books})