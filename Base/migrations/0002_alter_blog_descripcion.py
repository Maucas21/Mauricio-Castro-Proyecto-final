# Generated by Django 4.2 on 2023-06-01 19:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]