# Generated by Django 2.0.2 on 2018-03-21 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180314_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='num_comments',
        ),
    ]
