# Generated by Django 2.2.4 on 2021-10-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='movies.Actor'),
        ),
    ]