# Generated by Django 4.1.3 on 2022-11-23 16:23

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Название')),
                ('type', models.CharField(choices=[('TP', 'Топпинг'), ('BR', 'Ягоды'), ('DC', 'Декор')], db_index=True, max_length=2, verbose_name='Тип')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levels', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='Уровни')),
                ('shape', models.CharField(choices=[('CR', 'Круг'), ('SQ', 'Квадрат'), ('RC', 'Прямоугольник')], db_index=True, default='CR', max_length=2, verbose_name='Форма')),
                ('writing', models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Надпись')),
                ('comments', models.TextField(blank=True, verbose_name='Комментарии')),
                ('delivery_address', models.CharField(blank=True, db_index=True, max_length=100, verbose_name='Адрес доставки')),
                ('delivery_time', models.DateTimeField(db_index=True, verbose_name='Время доставки')),
                ('status', models.CharField(choices=[('10', 'Новый'), ('20', 'Запланирован'), ('30', 'Приготовление'), ('40', 'Доставка'), ('50', 'Исполнен'), ('90', 'Отменен')], db_index=True, default='10', max_length=2, verbose_name='Статус')),
                ('courier_info', models.TextField(blank=True, verbose_name='Информация для курьера')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('value', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Стоимость')),
                ('paid', models.BooleanField(db_index=True, default=False, verbose_name='Оплачен')),
                ('ingredients', models.ManyToManyField(blank=True, related_name='orders_used_in', to='bakecakeapp.ingredient', verbose_name='Ингредиент')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]