# Generated by Django 4.2.10 on 2024-02-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_story', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]
