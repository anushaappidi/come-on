# Generated by Django 4.0.4 on 2022-05-26 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_name',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher_name',
            new_name='user',
        ),
    ]
