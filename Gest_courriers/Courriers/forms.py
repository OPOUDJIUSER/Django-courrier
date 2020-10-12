from django import forms
from .models import Book

class BookForm(forms.ModelForm):
	publication_date = forms.DateTimeInput()
	class Meta:
		model = Book
		fields = "__all__"
