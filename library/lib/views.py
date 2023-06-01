from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import *
from .models import Books, Category
from.admin import BooksAdmin


class Categ:

    def get_category(self):
        category = Category.objects.all()
        return category


class Home(Categ, ListView):
    model = Books
    context_object_name = 'lib'
    template_name = 'lib/index.html'
    paginate_by = 9







class GetBook(DetailView):
    model = Books
    template_name = 'lib/book_p.html'
    context_object_name = 'lib'


class Catalog(Categ, ListView):
    model = Books
    template_name = 'lib/category.html'
    context_object_name = 'lib'
    paginate_by = 3

    def get_queryset(self):
        queryset = Books.objects.filter(category__slug=self.kwargs['slug'])
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class Search(ListView):
    template_name = 'lib/search.html'
    context_object_name = 'lib'
    paginate_by = 3

    def get_queryset(self):
        return Books.objects.filter(Q(title__icontains=self.request.GET.get('s'))
                                    | Q(author__icontains=self.request.GET.get('s')))





def addbook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddBookForm()

    return render(request, 'lib/add-book.html', {'form': form})
