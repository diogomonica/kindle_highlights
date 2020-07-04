# Generated by Django 3.0.7 on 2020-07-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=255)),
                ('subject', models.TextField(max_length=1000)),
                ('body', models.TextField()),
                ('received_at', models.DateTimeField(auto_now=True)),
                ('sender_email', models.EmailField(default='EMPTY_EMAIL', max_length=254)),
                ('attachment', models.TextField(default='')),
            ],
            options={
                'verbose_name_plural': 'emails',
            },
        ),
    ]
