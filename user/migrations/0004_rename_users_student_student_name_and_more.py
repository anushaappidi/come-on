# Generated by Django 4.0.4 on 2022-05-26 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_user_student_users_rename_user_teacher_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='users',
            new_name='student_name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='users',
            new_name='teacher_name',
        ),
    ]
