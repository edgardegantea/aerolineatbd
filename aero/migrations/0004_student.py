# Generated by Django 4.1.1 on 2022-10-27 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aero', '0003_alter_asiento_disponible'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]