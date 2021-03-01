from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class RuralGovernment(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name='Названия')
    image = models.ImageField(blank=True, null=True, default='rural_default.jpg', verbose_name='Картинка')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Местное правительство'
        verbose_name_plural = 'Местное правительство'


class Village(models.Model):
    name = models.CharField(max_length=40, verbose_name='Названия')
    image = models.ImageField(blank=True, null=True, default='defaultvillage.jpg', verbose_name='Картинка')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    ruralgovernment = models.ForeignKey(RuralGovernment, on_delete=models.CASCADE, verbose_name='Местное правительство')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Село'
        verbose_name_plural = 'Село'


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=40, verbose_name='Названия')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    phone = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='Названия')
    image = models.ImageField(blank=True, null=True, default='Changing-default-category.jpg')
    village = models.ForeignKey(Village, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


class SubCategory(models.Model):
    name = models.CharField(max_length=40, verbose_name='Названия')
    image = models.ImageField(blank=True, null=True, default='subcategorydefault.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегория'


class Image(models.Model):
    img = models.ImageField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
