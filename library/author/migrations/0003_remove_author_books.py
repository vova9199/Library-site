# Generated by Django 4.1 on 2023-10-15 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_alter_author_name_alter_author_patronymic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
    ]
