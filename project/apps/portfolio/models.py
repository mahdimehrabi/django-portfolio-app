from django.db import models

# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=35)
    title_fa = models.CharField('title persian', max_length=35)
    link = models.URLField()

    def __str__(self):
        return self.title


class Header(models.Model):
    first_title = models.CharField(max_length=80)
    first_title_fa = models.CharField(max_length=80)
    second_title = models.CharField(max_length=80)
    second_title_fa = models.CharField(max_length=80)
    background = models.ImageField(upload_to='images/')
