from django.db import models
from django.forms import FileField, ImageField

class proof(models.Model):
    full_name=models.CharField(max_length=100)
    dob =models.DateField(auto_now=False, auto_now_add=False)
    upload = ImageField( upload_to='static/proof', height_field=None, width_field=None, max_length=None)
    proof_type=models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

    
       
