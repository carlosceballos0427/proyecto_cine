# Generated by Django 4.1.2 on 2022-10-18 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0002_cliente_edad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='nombre',
            new_name='nombre_apellidos',
        ),
    ]
