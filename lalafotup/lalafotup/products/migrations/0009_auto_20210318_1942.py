# Generated by Django 3.1.7 on 2021-03-18 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0008_product_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категория'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товары', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='ruralgovernment',
            options={'verbose_name': 'Местное правительство', 'verbose_name_plural': 'Местное правительство'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Подкатегория', 'verbose_name_plural': 'Подкатегория'},
        ),
        migrations.AlterModelOptions(
            name='village',
            options={'verbose_name': 'Село', 'verbose_name_plural': 'Село'},
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Названия'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Названия'),
        ),
        migrations.AlterField(
            model_name='ruralgovernment',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='ruralgovernment',
            name='image',
            field=models.ImageField(blank=True, default='rural_default.jpg', null=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='ruralgovernment',
            name='name',
            field=models.CharField(max_length=40, unique=True, verbose_name='Названия'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Названия'),
        ),
        migrations.AlterField(
            model_name='village',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='village',
            name='image',
            field=models.ImageField(blank=True, default='defaultvillage.jpg', null=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='village',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Названия'),
        ),
        migrations.AlterField(
            model_name='village',
            name='ruralgovernment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ruralgovernment', verbose_name='Местное правительство'),
        ),
    ]
