from django.db import models


# Create your models here.

class RuralGovernment(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)


class Village(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True, null=True)
    ruralgoverment = models.ForeignKey(RuralGovernment,on_delete=models.SET_NULL,null=Truea)
