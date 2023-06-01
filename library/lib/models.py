from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Категорія')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категорії'
        verbose_name_plural = 'Категорії'



class Books(models.Model):
    title = models.CharField(max_length=50, verbose_name='Назва:')
    slug = models.SlugField(max_length=50, verbose_name='Url:', unique=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото:')
    author = models.CharField(max_length=50, verbose_name='Автор:')
    Genre = models.CharField(max_length=50, verbose_name='Жанр:')
    content = models.TextField( verbose_name='Опис:')
    availability = models.CharField(max_length=25, verbose_name='Наявність')
    number = models.IntegerField(default=0, verbose_name='Кількість:')
    category = models.ManyToManyField(Category,  related_name='books', verbose_name='Категорія:')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'



    def get_absolute_url(self):

        return reverse('book', kwargs={"slug": self.slug})
