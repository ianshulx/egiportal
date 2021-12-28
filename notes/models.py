from typing import Optional
from django.db import models
from django import forms
from django.db.models.enums import Choices

#bca notes

SEMSTERS_CHOICES=(
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    
)

UNIT_CHOICE=(
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
)



class bca_sem1_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name


class bca_sem2_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name


class bca_sem3_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name



class bca_sem4_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name


class bca_sem5_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name

class bca_sem6_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name


class btech_sem1_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name


class btech_sem2_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name

class btech_cs_sem3_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name

class btech_cs_sem4_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name


class btech_cs_sem5_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name

class btech_cs_sem6_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name

class btech_cs_sem7_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name

class btech_cs_sem8_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)
    
    def __str__(self):
        return self.UNIT_name

        #CE

class btech_ce_sem3_notes(models.Model):
        Subject=models.CharField(max_length=50)
        UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
        UNIT_name=models.CharField(max_length=150)
        Drive_link=models.URLField(max_length=2000)
    
        def __str__(self):
            return self.UNIT_name


class btech_ce_sem4_notes(models.Model):
        Subject=models.CharField(max_length=50)
        UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
        UNIT_name=models.CharField(max_length=150)
        Drive_link=models.URLField(max_length=2000)
    
        def __str__(self):
            return self.UNIT_name

class btech_ce_sem5_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)

    def __str__(self):
        return self.UNIT_name

class btech_ce_sem6_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)

    def __str__(self):
        return self.UNIT_name


class btech_ce_sem7_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)

    def __str__(self):
        return self.UNIT_name

class btech_ce_sem8_notes(models.Model):
    Subject=models.CharField(max_length=50)
    UNIT=models.CharField(max_length=50, choices=UNIT_CHOICE)
    UNIT_name=models.CharField(max_length=150)
    Drive_link=models.URLField(max_length=2000)

    def __str__(self):
        return self.UNIT_name



