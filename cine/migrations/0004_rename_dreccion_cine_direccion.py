# Generated by Django 4.1.2 on 2022-10-20 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0003_rename_nombre_cliente_nombre_apellidos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cine',
            old_name='dreccion',
            new_name='direccion',
        ),
    ]
