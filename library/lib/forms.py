from django import forms
from .models import *
from .admin import BooksAdmin


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'slug', 'photo', 'author', 'Genre', 'content', 'availability', 'number', 'category']


class SortBook(forms.Form):
    ordering = forms.ChoiceField(required=False, choices=[
        ["title", "Від А до Я"],
        ["-title", 'Від Я до А']
    ])

