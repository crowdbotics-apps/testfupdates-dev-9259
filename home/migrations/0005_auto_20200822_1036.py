# Generated by Django 2.2.15 on 2020-08-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_homepage_newapp"),
    ]

    operations = [
        migrations.RemoveField(model_name="homepage", name="body",),
        migrations.AddField(
            model_name="homepage", name="bodyjj", field=models.TextField(blank=True),
        ),
    ]
