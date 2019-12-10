from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

# Create your views here.

# displaying books in books.html, it fills the table
def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list
    }
    return render(request, 'books.html', context)
# displaying authors in authors.html, it fills the table
def authors(request):
    author_list = Author.objects.all()
    context = {
        'author_list': author_list,
    }
    return render(request, 'authors.html', context)

# This function creates a new book
def new_book(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect('/')
# This function creates a new author
def new_author(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')

# displaying book in book_info
def book_info(request, num):
    book = Book.objects.get(id=int(num))
    book_authors = book.authors.all()
    # all_authors = Author.objects.all()
    context = {
        'book': book,
        'book_authors': book_authors,
        # 'all_authors': all_authors
    }
    return render(request, 'book_info.html', context)
# displaying author in author_info
def author_info(request, num):
    author = Author.objects.get(id=int(num))
    # author_books = author.books.all()
    # all_books = Book.objects.all()
    context = {
        'author': author,
        # 'author_books': author_books,
        # 'all_books': all_books
    }
    return render(request, 'author_info.html', context)

# When adding book to author
def add_book(request, num):
    author_id = int(num)
    book_id_add = int(request.POST['book'])

    get_author = Author.objects.get(id=author_id)
    get_book = Book.objects.get(id=book_id_add)
    get_author.books.add(get_book)

    book_authors = book.authors.all()
    all_authors = Author.objects.all()
    context = {
        'book_authors': book_authors,
        'all_authors': all_authors
    }

    return redirect(f'authors/{num}')
# When adding author to book
def add_author(request, num):
    book_id = int(num)
    author_id_add = int(request.POST['author'])

    get_book = Book.objects.get(id=book_id)
    get_author = Author.objects.get(id=author_id_add)
    get_author.books.add(get_book)
    return redirect(f'/books/{num}')







