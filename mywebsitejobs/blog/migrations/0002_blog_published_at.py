# Generated by Django 3.2.5 on 2021-07-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
