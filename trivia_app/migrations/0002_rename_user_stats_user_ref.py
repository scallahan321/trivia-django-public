# Generated by Django 4.0.2 on 2022-03-09 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stats',
            old_name='user',
            new_name='user_ref',
        ),
    ]
