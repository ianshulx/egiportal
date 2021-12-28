from django.db import models


# Create your models here.
class notice(models.Model):
    title=models.CharField(max_length=100)
    notice= models.CharField(max_length=500)
    def __str__(self):
        return self.title

class notice1(models.Model):
    title=models.CharField(max_length=100)
    detail= models.CharField(max_length=2000)
    def __str__(self):
        return self.title





class quiz(models.Model):
    serial=models.IntegerField(models.AutoField(("1")))
    last_date=models.DateField(auto_now=False, auto_now_add=False)
    quiz_name= models.CharField(max_length=150)
    quiz_link= models.URLField(max_length=200)
    def __str__(self):
        return self.quiz_name


class book(models.Model):
    book_name=models.CharField(max_length=50)
    author=models.CharField( max_length=50)
    forstudent=models.CharField(max_length=50)
    def __str__(self):
        return self.book_name

class image(models.Model):
    event_name=models.CharField(max_length=50)
    pic=models.ImageField(upload_to='static/images/student_gallry', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.event_name

class event1(models.Model):
    event_name=models.CharField(max_length=50)
    event_date=models.DateField(auto_now=False, auto_now_add=False)
    event_link=models.URLField(max_length=200)
    poster=models.ImageField(upload_to="static/event_posters", height_field=None, width_field=None, max_length=None)
    details=models.CharField( max_length=500)

    def __str__(self):
        return self.event_name

class Main_Event(models.Model):
    event_name=models.CharField(max_length=50)
    event_date=models.DateField(auto_now=False, auto_now_add=False)
    event_link=models.URLField(max_length=200)
    
    details=models.CharField( max_length=500)

    def __str__(self):
        return self.event_name







    



