# Generated by Django 2.2.1 on 2019-06-04 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mathsQuiz', '0002_auto_20190604_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='questionSet',
            new_name='Question Set',
        ),
    ]