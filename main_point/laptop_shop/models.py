from django.db import models
from .mixins import GoogleDriveFileMixin
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

class Collection(GoogleDriveFileMixin, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='main_point/media/collections/images/', storage=gd_storage)

    def __str__(self):
        return self.name

class Product(GoogleDriveFileMixin, models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='main_point/media/product/images/', storage=gd_storage)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
