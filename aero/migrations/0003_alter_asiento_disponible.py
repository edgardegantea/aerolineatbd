# Generated by Django 4.1.1 on 2022-10-18 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aero', '0002_alter_boleto_clase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asiento',
            name='disponible',
            field=models.CharField(choices=[('Libre', 'Libre'), ('Ocupado', 'Ocupado')], default='Libre', max_length=7, verbose_name='Seleccione la disponibilidad del asiento'),
        ),
    ]
