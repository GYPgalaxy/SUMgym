# Generated by Django 3.1.4 on 2021-01-01 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_auto_20210101_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='course_name',
        ),
    ]
