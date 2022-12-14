# Generated by Django 4.1.3 on 2022-11-24 19:35

from django.db import migrations


class Migration(migrations.Migration):

    def add_empty_values(apps, schema_editor):
        ingredient = apps.get_model('bakecakeapp', 'Ingredient')
        ingredient.objects.filter(type="TP", name="Без").delete()
        ingredient.objects.bulk_create([
            ingredient(type="TP", name="Нет", price=0),
            ingredient(type="BR", name="Нет", price=0),
            ingredient(type="DC", name="Нет", price=0),
        ])

    dependencies = [
        ('bakecakeapp', '0006_order_payment_id'),
    ]

    operations = [
        migrations.RunPython(add_empty_values),
    ]
