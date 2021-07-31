from django.db import models


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


class HeaderButton(models.Model):
    title = models.CharField(max_length=60)
    title_fa = models.CharField(max_length=60)
    Header = models.ForeignKey(Header, on_delete=models.CASCADE)
    link = models.URLField()


class About(models.Model):
    text = models.TextField()
    text_fa = models.TextField()

    def __str__(self):
        return 'about me'
