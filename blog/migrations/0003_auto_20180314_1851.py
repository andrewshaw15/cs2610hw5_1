# Generated by Django 2.0.2 on 2018-03-15 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180314_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='num_comments',
        ),
        migrations.AddField(
            model_name='blog',
            name='num_comments',
            field=models.IntegerField(default=0),
        ),
    ]