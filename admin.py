from django.contrib import admin
from .models import Category, Product, Identifiant


# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display = ['name', 'date_added']

class AdminProduct(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'date_added']

class AdminIdentifiant(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'second_name', 'mail', 'number', 'password', 'date_added']


admin.site.register(Category, AdminCategorie)
admin.site.register(Product, AdminProduct)
admin.site.register(Identifiant, AdminIdentifiant)
