# Generated by Django 3.2.3 on 2021-12-14 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articolo',
            options={'verbose_name': 'Articolo', 'verbose_name_plural': 'Articoli'},
        ),
        migrations.AlterModelOptions(
            name='giornalista',
            options={'verbose_name': 'Giornalista', 'verbose_name_plural': 'Giornalisti'},
        ),
    ]
