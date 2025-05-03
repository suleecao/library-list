from django import forms
from .models import UserBook

class UserBookForm(forms.ModelForm):
    class Meta:
        model = UserBook
        fields = ['date', 'is_read']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'is_read': forms.CheckboxInput(),
        }
