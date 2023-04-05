from django.conf import settings
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
        }




class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    categoryid = models.IntegerField(default=0)
    def to_json(self):
        return {
            'id':self.id,
            'name' :self.name,
            'price' :self.price,
            'description':self.description,
            'count':self.count,
            'is_active':self.is_active,
            'categoryid':self.categoryid,
        }