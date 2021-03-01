from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','date_created']

admin.site.register(RuralGovernment)
admin.site.register(Village)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image)

class ProductInline(admin.TabularInline):
    model = Product



class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


admin.site.register(SubCategory,CategoryAdmin)
admin.site.register(Category)
