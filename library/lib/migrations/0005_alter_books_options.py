# Generated by Django 4.1.2 on 2022-11-03 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0004_remove_books_data_alter_books_genre_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['title'], 'verbose_name': 'Client Logo', 'verbose_name_plural': 'Client Logos'},
        ),
    ]