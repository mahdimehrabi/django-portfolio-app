# Generated by Django 3.2.5 on 2021-07-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='title_fa',
            field=models.CharField(default='persian title', max_length=35, verbose_name='title persian'),
            preserve_default=False,
        ),
    ]
