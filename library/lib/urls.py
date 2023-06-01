from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>', Catalog.as_view(), name='category'),
    path('book/<str:slug>/', GetBook.as_view(), name='book'),
    path('search/', Search.as_view(), name='search'),
    path('addbook/', views.addbook, name='addbook')

]
