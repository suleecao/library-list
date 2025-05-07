from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    rating = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="0–5 stars",
    )
    UserBook = models.ManyToManyField(User, through='UserBook', related_name='books')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'book_id': self.id})
    


class UserBook(models.Model):
    date = models.DateField("date finished")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    recommend  = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'book')  

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='user_books')

    def __str__(self):
        return f"{self.user.username} - {self.book.title} {self.date} { self.recommend}"