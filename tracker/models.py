from django.db import models

# Create your models here.
class Tracker(models.Model):
    status = models.CharField(max_length= 6, null=False, blank=False)
    ticker = models.CharField(max_length= 8, null=False, blank=False) 
    position = models.CharField(max_length= 4, null=False, blank=False)
    date_opened = models.DateField(null=False, blank=False) 
    amount_traded = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False) 
    opening_price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    closing_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    date_closed = models.DateField(null=True, blank=True)
    profit_loss = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    result = models.CharField(max_length= 4, null=True, blank=True) 
