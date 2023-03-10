# Generated by Django 3.2 on 2023-01-31 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bangla', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
