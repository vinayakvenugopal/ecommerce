# Generated by Django 3.2.14 on 2022-07-17 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sTock',
            new_name='stock',
        ),
    ]
