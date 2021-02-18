from django.db import models


# Create your models here.

class RuralGovernment(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Village(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    ruralgovernment = models.ForeignKey(RuralGovernment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField()
    description = models.TextField(blank=True, null=True)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
