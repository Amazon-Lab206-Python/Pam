# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Review, Author, Book, User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "book_reviews/index.html")

def register(request):
    result = User.objects.validate_reg(request.POST)
    if result[0] == False:
        for error in result[1]:
            messages.error(request, error)
        return redirect("/")
    else:
        request.session['user_id'] = User.objects.get(email=request.POST['email']).id
        return redirect("/users/{}".format(request.session['user_id']))

def login(request):
    result = User.objects.validate_login(request.POST)
    if result[0] == False:
        for error in result[1]:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = User.objects.get(email=request.POST['email']).id
        return redirect("/users/{}".format(request.session['user_id']))

def books(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']).name,
        'recent': Review.objects.recent_and_not()[0],
        'more': Review.objects.recent_and_not()[1]
    }
    return render(request, "book_reviews/books.html", context)

def add(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "book_reviews/add.html", context)

def create_new(request):
    user_id = request.session['user_id']
    result = Review.objects.validate_review(request.POST, user_id)
    if result[0] == False:
        for error in result[1]:
            messages.error(request, error)
        return redirect("/books/add")
    else:
        book_id = Review.objects.get(title=request.POST['title']).id
        return redirect ("/books/{}".format(book_id))

def add_new(request, book_id):
    user_id = request.session['user_id']
    book = Book.objects.get(id=book_id)
    book_data = {
        'title': book.title,
        'author': book.author,
        'rating': request.POST['rating'],
        'review': request.POST['review']
    }
    result = Review.objects.validate_review(book_data, user_id)
    if result[0] == False:
        for error in result[1]:
            messages.error(request, error)
    return redirect("/books/{}".format(book_id))
    
def book_info(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'review': Review.objects.filter(book=book_id)
    }
    return render(request, "book_reviews/book_info.html", context)

def user_info(request, user_id):
    user = User.objects.get(id=user_id)
    unique_ids = user.user_reviews.all().values("book").distinct()
    unique_books = []
    for book in unique_ids:
        unique_books.append(Book.objects.get(id=book['book']))
    context = {
        'user': User.objects.get(id=user_id),
        'unique_book_reviews': unique_books
    }
    return render(request, "book_reviews/user_info.html", context)

def destroy(request, review_id):
    Review.objects.get(id=review_id).delete()
    return redirect(request, "/books")

def logout(request):
    del request.session['user_id']
    return redirect('/')
