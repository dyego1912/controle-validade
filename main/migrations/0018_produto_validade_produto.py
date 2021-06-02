# Generated by Django 3.2 on 2021-04-20 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210420_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True)),
                ('codigo_barras', models.IntegerField(unique=True)),
                ('descricao', models.CharField(max_length=255)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=6)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Validade_Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_validade', models.DateField()),
                ('quantidade', models.IntegerField()),
                ('codigo_barras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.produto')),
                ('conferencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.conferencia')),
            ],
        ),
    ]