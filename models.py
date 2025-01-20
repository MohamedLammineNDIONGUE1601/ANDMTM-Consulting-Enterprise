from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title

class Identifiant(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-second_name']
    
    def __str__(self):
        return self.second_name

# Optional: You can add a model to track PayPal transactions if needed
class PayPalTransaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=200)
    amount = models.FloatField()
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return f"Transaction {self.transaction_id} for {self.product.title}"
