from django.db import models

from menu_items.models import Menu_item


class Recipt(models.Model):
    name = models.CharField('name', max_length=100)
    total_price = models.FloatField('total_price')
    # total_price_discount = Column('total_price', Integer) todo
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}  {self.total_price} {self.date}'


class Orders(models.Model):
    status = [
        ('order', 'Order'),
        ('kitchen', 'Kitchen'),
        ('ready', 'Ready'),
        ('serve', 'Serve'),
    ]
    statuses = models.CharField('status', choices=status, max_length=15)
    number = models.IntegerField('Order_number')
    date = models.DateField('date', auto_now=False, auto_now_add=False)
    order = models.ForeignKey(Recipt, verbose_name='recipt_id', related_name='Orders',
                              on_delete=models.CASCADE, null=True)
    order_menu = models.ManyToManyField(Menu_item)

    def __str__(self):
        return self.status
