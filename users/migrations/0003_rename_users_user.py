# Generated by Django 4.1.4 on 2022-12-23 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]