# Generated by Django 3.0.7 on 2020-07-28 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('highlights', '0005_auto_20200727_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='volume',
            name='authors',
            field=models.TextField(default=''),
        ),
    ]
