from django.db import models


class Author(models.Model):
    nationals = [
        ('us', 'usa'),
        ('Ir', 'Iran'),
        ('en', 'English'),
    ]
    name = models.CharField()
    surname = models.CharField()
    birth_date = models.IntegerField()
    death_year = models.IntegerField()
    nationality = models.CharField(choices=nationals)


class Language(models.Model):
    title = models.CharField()
    spoken = models.CharField()


class Book(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    languages = models.ManyToManyRel
# class Author(models.Model):
# nationals = [
# ('us','American'),
# ('ir', 'Iranian'),
# ('uk', 'English'),
# ('du', 'Germany'),
# ('ru', 'Russia')
# ]
# name = models.CharField(max_length=250)
# surname = models.CharField(max_length=250)
# birth_year = models.IntegerField()
# death_year = models.IntegerField()
# nationality = models.CharField(max_length=2, choices=nationals)
# class Language(models.Model):
# title = models.CharField(max_length=250
# spoken_countries = models.CharField(max_length=250)
# class Book(models.Model):
# title = models.CharField(max_length=250)
# author = models.ForeignKey(Author, on_delete=models.CASCADE)
# publication_date = models.DateField()
# publisher = models.CharField(max_length=250)
# language = models.ManyToManyField(Language)
# from django.utils.text import slugify