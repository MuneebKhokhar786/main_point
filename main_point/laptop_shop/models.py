from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='laptop_shop/static/laptop_shop/images/collections/', null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
