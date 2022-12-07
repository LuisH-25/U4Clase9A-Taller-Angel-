from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from .models import Book

class BookList(ListView):
    model = Book
    template_name = "booklist.html"
    