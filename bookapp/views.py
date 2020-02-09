from django.shortcuts import render, HttpResponse, redirect
from bookapp.models import Book, Author

def index(request):
    books = []
    for b in Book.objects.all():
        books.append(b)
    context = {
        "books" : books
    }
    return render(request, "index.html", context)

def addbook(request):
    title=request.POST["title"].strip()
    if title == "": return redirect("/")
    existing = Book.objects.filter(title=title).count()
    if existing > 0: return redirect("/")

    desc=request.POST["desc"].strip()
    Book.objects.create(title=title, desc=desc)
    return redirect("/")

def book(request, id):
    b = Book.objects.get(id=id)
    available_authors = []
    for a in Author.objects.all():
        ct = a.books.filter(id=id).count()
        if ct == 0:
            available_authors.append(a)
    context = { 
        "book" : b,
        "available_authors" : available_authors
    }
    return render(request, "single-book.html", context)

def authors(request):
    authors=[]    
    for a in Author.objects.all():
        authors.append(a)
    context = {
        "authors" : authors
    }
    return render(request, "authors.html", context)

def addauthor(request):
    firstname=request.POST["firstname"].strip()
    lastname=request.POST["lastname"].strip()
    if firstname == "" or lastname == "": return redirect("/authors")
    existing = Author.objects.filter(first_name=firstname, last_name=lastname).count()
    if existing > 0: return redirect("/authors")

    notes=request.POST["notes"].strip()
    Author.objects.create(first_name=firstname, last_name=lastname, notes=notes)
    return redirect("/authors")

def author(request, id):
    a = Author.objects.get(id=id)   
    available_books = []
    for b in Book.objects.all():
        ct = b.authors.filter(id=id).count()
        if ct == 0:
            available_books.append(b)
    
    context = { 
        "author" : a,
        "available_books" : available_books
    }
    return render(request, "single-author.html", context)

def addBookToAuthor(request):
    associate(request)
    aid = request.POST["author_id"]
    return redirect(f"/author/{aid}")

def addAuthorToBook(request):
    associate(request)
    bid = request.POST["book_id"]
    return redirect(f"/book/{bid}")

def associate(request):
    bid = request.POST["book_id"]
    aid = request.POST["author_id"]
    b = Book.objects.get(id=bid)
    a = Author.objects.get(id=aid)
    b.authors.add(a)

