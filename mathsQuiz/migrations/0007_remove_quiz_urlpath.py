# Generated by Django 2.2.1 on 2019-06-13 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mathsQuiz', '0006_auto_20190611_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='urlpath',
        ),
    ]
