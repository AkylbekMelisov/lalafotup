from django.db import models


# Create your models here.

class RuralGovernment(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)


class Village(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    ruralgovernment = models.ForeignKey(RuralGovernment,on_delete=models.CASCADE,null=True)



class Product(models.Model):
    sub_categories = (
        ('car','car'),
        ('trucks','trucks'),
        ('chicken','chicken'),
        ('duck','duck'),
        ('goose','goose'),
        ('turkey','turkey'),
    )
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True,null=True)
    sub_category = models.CharField(max_length=40,choices=sub_categories)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=40)
    village = models.ForeignKey(Village,on_delete=models.CASCADE,null=True)