from django.db import models
from django.urls import reverse
# Create your models here.
class Inventory(models.Model):
    stockNumber = models.CharField(max_length=200)
    quantity = models.IntegerField()
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    partName = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)


    @property
    def get_html_url(self):
        url = reverse('inventory_edit',args=(self.id,))
        return f'<a href="{url}"> {self.stockNumber}</a>'

    def updateNum(self,num):
        self.quantity -= num
        self.save()

    def __str__(self):
        return "{}: {}".format(self.type,self.partName)