from django.db import  models

class Contactus(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    state=models.CharField(max_length=40)
    subject=models.CharField(max_length=100)



    class Meta:
        db_table = 'queries'