from django.db import models

# Create your models here.
class project(models.Model):
    Project_name=models.CharField(max_length=100)
    Github_link=models.URLField(max_length=500)
    Project_image=models.ImageField( upload_to='static/images', height_field=None, width_field=None, max_length=None)
    
       
    def __str__(self):
        return self.Project_name
