from django.db import models
from cloudinary.models import CloudinaryField
from .mixins import CloudinaryImageMixin


class Collection(CloudinaryImageMixin, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', folder='main_point/collections/images/',
                            transformation={
                                'width': 600,
                                'height': 400,
                                'crop': 'fill',
                            })

    def __str__(self):
        return self.name


class Product(CloudinaryImageMixin, models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', folder='main_point/products/images/',
                            transformation={
                                'width': 600,
                                'height': 600,
                                'crop': 'fill',
                            })
    collection = models.ForeignKey(
        Collection, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
