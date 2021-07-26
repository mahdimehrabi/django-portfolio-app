from django.db import models

# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=35)
    title_fa = models.CharField('title persian', max_length=35)
    link = models.URLField()

    def __str__(self):
        return self.title
