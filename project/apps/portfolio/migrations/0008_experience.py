# Generated by Django 3.2.5 on 2021-07-31 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_about_text_fa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_name', models.CharField(max_length=80)),
                ('job_title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('employer_name_fa', models.CharField(max_length=80)),
                ('job_title_fa', models.CharField(max_length=60)),
                ('description_fa', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]