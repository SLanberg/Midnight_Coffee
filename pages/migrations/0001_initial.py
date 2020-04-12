# Generated by Django 3.0.4 on 2020-04-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('text', models.TextField(default='page/index.html', max_length=500)),
                ('active', models.TextField(verbose_name='Text Field')),
                ('template', models.CharField(default='page/index.html', max_length=500)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='url')),
            ],
        ),
    ]