from django.db import models

# Create your models here.
class Tamazon(models.Model):
    item_name = models.CharField(max_length=50,unique=True)
    item_rating = models.CharField(max_length=1000)
    item_offers = models.CharField(max_length=255,default="email")
    item_price = models.IntegerField(default=0)
    item_features = models.CharField(max_length=1000)

    class Meta():
        db_table="Tamazon"
        verbose_name_plural = "Tamazon"

    def __str__(self):
        return self.item_name

