from django.shortcuts import render, redirect
from .models import MyBooks

def index(request) :
    books = MyBooks.objects.all()
    context = {
        'books' : books,
    }
    return render(request, 'users/index.html', context)

def detail(request, pk) :
    book = MyBooks.objects.get(pk = pk)
    context = {
        'book' : book,
    }
    return render(request, 'users/detail.html', context)

def new(request) :
    return render(request, 'users/new.html')

def create(request) :
    title = request.POST.get('title')
    status = request.POST.get('status')
    rating = request.POST.get('rating')
    review = request.POST.get('review')

    book = MyBooks(title = title, status = status, rating = rating, review = review)
    book.save()

    return redirect('users:detail', book.pk)

def delete(request, pk) :
    book = MyBooks.objects.get(pk = pk)
    book.delete()
    return redirect('users:index')

def edit(request, pk) :
    book = MyBooks.objects.get(pk = pk)
    context = {
        'book' : book
    }
    return render(request, 'users/edit.html', context)

def update(request, pk) :
    book = MyBooks.objects.get(pk = pk)

    title = request.POST.get('title')
    status = request.POST.get('status')
    rating = request.POST.get('rating')
    review = request.POST.get('review')

    book.title = title
    book.status = status
    book.rating = rating
    book.review = review
    book.save()

    return redirect('users:detail', book.pk)
    