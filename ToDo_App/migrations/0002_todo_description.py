# Generated by Django 4.2.11 on 2024-09-28 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
