# Generated by Django 4.1.3 on 2022-11-23 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakecakeapp', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
    ]
