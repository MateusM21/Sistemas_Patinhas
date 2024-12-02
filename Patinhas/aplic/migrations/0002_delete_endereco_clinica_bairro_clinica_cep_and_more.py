# Generated by Django 4.2.16 on 2024-12-01 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Endereco',
        ),
        migrations.AddField(
            model_name='clinica',
            name='bairro',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='clinica',
            name='cep',
            field=models.IntegerField(blank=True, null=True, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='clinica',
            name='cidade',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='clinica',
            name='complemento',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Complemento'),
        ),
        migrations.AddField(
            model_name='clinica',
            name='estado',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='clinica',
            name='logradouro',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Logradouro'),
        ),
        migrations.AddField(
            model_name='clinica',
            name='numero_logradouro',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número'),
        ),
    ]
