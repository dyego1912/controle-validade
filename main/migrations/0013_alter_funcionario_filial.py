# Generated by Django 3.2 on 2021-04-20 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_corredor_filial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='filial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='filial_funcionario', to='main.filial'),
        ),
    ]
