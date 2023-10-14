from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'main/books.html', {'books':books})