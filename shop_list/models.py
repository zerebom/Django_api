from django.db import models

# Create your models here.

class Shoptext(models.Model):
    restaurant_name=models.CharField(max_length=200)
    restaurant_id=models.IntegerField()
    description=models.TextField()
    menus=models.TextField()


class Shop_feature_values(models.Model):
    feature_1=models.FloatField()
    label=models.IntegerField()



