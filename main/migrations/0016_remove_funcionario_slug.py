# Generated by Django 3.2 on 2021-04-20 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210420_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='slug',
        ),
    ]
