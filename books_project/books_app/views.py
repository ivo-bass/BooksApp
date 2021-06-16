from books_project.books_app.forms import BookForm
from django.shortcuts import redirect, render
from books_project.books_app.models import Book


def show_books_form(request, form, template_name):
    context = {'form': form}
    return render(request, template_name, context)


def save_book_from_form(request, form, template_name, redirect_view):
    if form.is_valid():
        form.save()
        return redirect(redirect_view)
    return show_books_form(request, form, template_name)


# ___________VIEWS___________

def index(request):
    context = {'books': Book.objects.all(), }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'GET':
        form = BookForm()
        return show_books_form(request, form, 'create.html')
    else:
        form = BookForm(request.POST)
        return save_book_from_form(request, form, 'create.html', index)


def edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
        return show_books_form(request, form, 'edit.html')
    else:
        form = BookForm(request.POST, instance=book)
        return save_book_from_form(request, form, 'edit.html', index)


def delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect(index)
