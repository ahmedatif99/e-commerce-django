# Generated by Django 4.2.1 on 2023-05-30 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.RenameField(
            model_name='address',
            old_name='appartment_address',
            new_name='apartment_address',
        ),
    ]
