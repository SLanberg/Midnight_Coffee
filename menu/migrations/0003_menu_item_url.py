# Generated by Django 3.0.4 on 2020-04-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200411_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_item',
            name='url',
            field=models.CharField(max_length=100, null=True, verbose_name='External resource url'),
        ),
    ]