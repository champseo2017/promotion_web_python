from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from book_management.models import Category, Book


# Create your views here.

def index(request):
    context = {
        'book_num': len(Book.objects.all()),
        'cat_num': len(Category.objects.all()),
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)
