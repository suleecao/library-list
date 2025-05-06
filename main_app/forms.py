from django import forms
from .models import UserBook

class UserBookForm(forms.ModelForm):
    class Meta:
        model = UserBook
        fields = ['date', 'recommend']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'recommend': forms.CheckboxInput(),
        }
