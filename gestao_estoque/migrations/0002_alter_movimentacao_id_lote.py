# Generated by Django 3.2.8 on 2021-11-17 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='id_lote',
            field=models.ForeignKey(blank=True, default='Único', on_delete=django.db.models.deletion.CASCADE, to='gestao_estoque.lotes'),
        ),
    ]
