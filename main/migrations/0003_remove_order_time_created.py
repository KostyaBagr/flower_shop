# Generated by Django 4.2.2 on 2023-06-16 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='time_created',
        ),
    ]
