from django.db import models
from datetime import datetime

# Create your models here.
class Stockx(models.Model):
    
    item_name=models.CharField(max_length=50, null = True, blank=True)
    stock_branch_name=models.CharField(max_length=50, null = True, blank=True)
    stock_type=models.CharField(max_length=50, null = True, blank=True)
    stock_time_of_produce=models.CharField(max_length=50, null = True, blank=True)
    stock_contact=models.CharField(max_length=50, null = True, blank=True)
    stock_source = models.CharField(max_length=50, null = True, blank=True)
    unit_cost = models.IntegerField(default=10, null = True, blank=True)
    unit_price = models.IntegerField(default=0, null = True, blank=True)
    total_quantity = models.IntegerField(default=0, null = True, blank=True)
    issued_quantity = models.IntegerField(default=0, null = True, blank=True)
    def __str__(self):
        return self.item_name

   
#we have created one classs that suites a given table
#above is a table head

#used by the sales agent.
# associating property "item" wz the stock kept in the "Stockx" model or table.
class Sales(models.Model):
    branch_name = models.CharField(max_length=50, null =True, blank=True)
    seller = models.CharField(max_length=50, null =True, blank=True)
    item = models.ForeignKey(Stockx, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=10, null=True, blank=True)
    amount_received = models.IntegerField(default=10, null=True, blank=True)
    issued_to = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.IntegerField(default=10, null=True, blank=True)
    date = models.DateField(default=datetime.now())


#defining a method

    def get_total(self):
        # Ensure both quantity and unit_price are valid
        if self.quantity is None or self.item.unit_price is None:
            return 0  # Return 0 if either value is None
        total = self.quantity * self.item.unit_price
        return int(total)




    def get_change(self):
        if self.quantity is None or self.item.unit_price is None:
            return 0 
        change = self.get_total() - self.amount_received
        return abs(int(change))
    

    def __str__(self):
        return self.item.item_name


class Deffered_payments(models.Model):
    customer_name = models.CharField(max_length=50, null=True, blank=True)
    contact = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    nin = models.CharField(max_length=50, null=True, blank=True)
    item_bought_on_credit = models.CharField(max_length=50, null=True, blank=True)
    quantity = models.IntegerField(default=10, null=True, blank=True)
    unit_price = models.IntegerField(default=10, null=True, blank=True)
    amount = models.IntegerField(default=0, null=True, blank=True)
    balance = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateField(default=datetime.now())
    date_of_payment = models.DateField(default=datetime.now())
    branch = models.CharField(max_length=50, null=True, blank=True)
    agent = models.CharField(max_length=50, null=True, blank=True)



    def __str__(self):
        return self.customer_name