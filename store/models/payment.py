from django.db import  models

class Payment(models.Model):
    card_number=models.CharField(max_length=15)
    expiry=models.CharField(max_length=10)
    cvv=models.CharField(max_length=5)
    card_holder=models.CharField(max_length=40,default="", editable=False)



    class Meta:
        db_table = 'payments'