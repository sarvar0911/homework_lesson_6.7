from django.urls import path
from my_app import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('books/', views.books, name='books'),
    path('browse/', views.browse, name='browse'),
    path('reading_nook/', views.reading_nook, name='reading_nook'),
    path('author_spotlight/', views.author_spotlight, name='author_spotlight'),
    path('events/', views.events, name='events'),
    path('community_corner/', views.community_corner, name='community_corner'),
]
