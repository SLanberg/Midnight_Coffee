# Generated by Django 3.0.4 on 2020-04-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200410_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='url'),
        ),
    ]
