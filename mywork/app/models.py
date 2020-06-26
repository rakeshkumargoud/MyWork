from django.db import models

class ClientProfile(models.Model):
    id=models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    address=models.CharField(max_length=255)
    contact=models.IntegerField(unique=True,default=False)
    email=models.EmailField(max_length=33)
    password=models.CharField(max_length=20,default=False)
    business_profile=models.CharField(max_length=244)


