# Generated by Django 4.1.1 on 2022-10-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleto',
            name='clase',
            field=models.CharField(max_length=10, verbose_name='Ingrese el tipo de clase del boleto'),
        ),
    ]
