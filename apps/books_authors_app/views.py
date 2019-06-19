from django.shortcuts import render, HttpResponse, redirect
from .models import book
from .models import author

def index(request):
    context = {
        "books" : book.objects.all(),
        "authors" : author.objects.all()
    }
    return render(request,'books_authors_app/add_book.html', context)

def add_books(request):
    book.objects.create(title= request.POST["title"], desc = request.POST["desc"])
    return redirect('/')

def go_to_books(request, book_id):
    context = {
        "books" : book.objects.all(),
        "book" : book.objects.get(id=book_id),
        "authors" : author.objects.all(),
        "author" : book.objects.get(id=book_id).author.all()
    }
    return render(request,"books_authors_app/books_author.html", context, book_id)

# def insert_author(request, author_id):
#     grab = models.author.objects.get(id=author_id) #this get the author from the selected id 
#     models.author.objects.add() #add that user to the list of authors 
#     return redirect('/books/{{book.id}}')
# # Create your views here.

def insert_author(request):
    if request.method == 'POST':
        book_id = request.POST["book_id"]
        author_id = request.POST["author_id"]
        book.objects.get(id=book_id).author.add(author.objects.get(id=author_id))
    return redirect("/books/"+book_id)

def author_page(request):
    context = {
        "books" : book.objects.all(),
        "authors" : author.objects.all()
    }
    return render(request,'books_authors_app/add_author.html', context)

def add_authors(request):
    author.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], note = request.POST["notes"])
    return redirect('/go_to_author')

def go_to_authors(request, author_id):
    context = {
        "authors" : author.objects.all(),
        "author" : author.objects.get(id=author_id),
        "books" : book.objects.all(),
        "book" : author.objects.get(id=author_id).books.all()
    }
    return render(request,"books_authors_app/authors_book.html", context, author_id)

def insert_book(request):
    if request.method == 'POST':
        book_id = request.POST["book_id"]
        author_id = request.POST["author_id"]
        author.objects.get(id=author_id).books.add(book.objects.get(id=book_id))
    return redirect("/author/"+author_id)