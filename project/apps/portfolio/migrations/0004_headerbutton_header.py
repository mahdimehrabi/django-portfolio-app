# Generated by Django 3.2.5 on 2021-07-28 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_header_headerbutton'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerbutton',
            name='Header',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portfolio.header'),
            preserve_default=False,
        ),
    ]