from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from .models import Book

from django.core.paginator import Paginator

class BookList(ListView):
    model = Book
    template_name = "booklist.html"
    paginate_by = 10        # numero de libros por lagina

def listing(request):
    book_list = Book.objects.all()
    print(book_list)
    paginator = Paginator(book_list,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'booklist.html',{'page_obj':page_obj})