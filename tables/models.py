from django.db import models
from orders.models import Orders
class Tables(models.Model):
    position = models.CharField(max_length=255)
    number = models.IntegerField()
    order=models.ManyToManyField(Orders)

    def __str__(self):
        return self.position+":"+str(self.number)
