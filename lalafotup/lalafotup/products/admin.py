from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','sub_category','date']

admin.site.register(RuralGovernment)
admin.site.register(Village)
admin.site.register(Product,ProductAdmin)

class ProductInline(admin.TabularInline):
    model = Product
    fk_name = "category"


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


admin.site.register(Category,CategoryAdmin)
