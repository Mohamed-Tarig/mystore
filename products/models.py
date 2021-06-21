from django.db import models
from django.db.models.fields import CharField, TextField
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = CharField(max_length=100)
    description = TextField(max_length=500, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('product_details', args=(self.id,))

    def __str__(self):
        return self.title