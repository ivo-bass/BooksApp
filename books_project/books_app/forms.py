from django.forms import fields, widgets
from books_project.books_app.models import Book
from django import forms
from django.core.exceptions import ValidationError


class BootstrapMixin:
    def _init_bootstrap(self):
        for _, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
            }


class BookForm(forms.ModelForm, BootstrapMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(),
        }
