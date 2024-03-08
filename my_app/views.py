from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from my_app.models import Book

from django.shortcuts import render


def home(request):
    return render(request, 'my_app/index.html')


def about(request):
    return HttpResponse('About section.')


def books(request):
    books = Book.objects.all()
    context = {'ajoyib_kitoblar': books}
    return render(request, 'my_app/books.html', context)


def browse(request):
    return render(request, 'my_app/browse.html')


def reading_nook(request):
    return render(request, 'my_app/reading_nook.html')


def author_spotlight(request):
    return render(request, 'my_app/author_spotlight.html')


def events(request):
    return render(request, 'my_app/events.html')


def community_corner(request):
    return render(request, 'my_app/community_corner.html')
