from django.db import models

# Create your models here.

class User(models.Model):
    category = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    family_arabic = models.CharField(max_length=200)
    family_english = models.CharField(max_length=200)
    fullname_arabic = models.CharField(max_length=200)
    fullname_english = models.CharField(max_length=200)
    birth_date = models.DateField(max_length=200)
    birth_place = models.CharField(max_length=200)
    
    nick_name = models.CharField(max_length=200)
    
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    
    
    type = models.CharField(max_length=200)
    document_number = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    from_date = models.DateField(max_length=200)
    to_date = models.DateField(max_length=200)
    
    other_information = models.CharField(max_length=200)
    
    