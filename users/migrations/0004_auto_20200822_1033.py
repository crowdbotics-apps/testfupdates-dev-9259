# Generated by Django 2.2.15 on 2020-08-22 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_user2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user2',
            new_name='user2tes',
        ),
    ]