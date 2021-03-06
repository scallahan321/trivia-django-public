# Generated by Django 4.0.2 on 2022-03-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia_app', '0005_rename_c9_correct_stats_correct_answers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='cat10_attempted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stats',
            name='cat10_correct',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stats',
            name='cat9_attempted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stats',
            name='cat9_correct',
            field=models.IntegerField(default=0),
        ),
    ]
