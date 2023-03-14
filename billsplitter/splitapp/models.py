from django.db import models
from django.contrib.auth.models import Group


# Create your models here.

class Bill:
    b_name = models.CharField(max_length=70)
    def add_item():
        item_name = models.CharField(max_length=70)
        item_qty = models.IntegerField()
        item_price = models.IntegerField()
        item = [item_name, item_qty, item_price]
        bill = payment.bill_calc(item_qty,item_price)


class create_grp:
    grp_name = models.CharField(max_length=70)
    group = Group.objects.create(name= grp_name)

class add_parti:
    parti_name = models.CharField()
    parti = models.ManyToManyField(create_grp)
    create_grp.group.user_set.add(parti_name)
    

class payment:
    def bill_calc(item_qty, item_price):
        amount = item_qty*item_price
        no_of_parti = len(create_grp.group)
        split_bill  = amount/no_of_parti
        return split_bill
