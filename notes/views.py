from django.shortcuts import render
from django.http import HttpRequest
from django.http import request
from .models import bca_sem1_notes ,bca_sem6_notes ,bca_sem5_notes,bca_sem4_notes ,bca_sem3_notes ,bca_sem2_notes, btech_cs_sem3_notes, btech_sem1_notes,btech_sem2_notes
from .models import btech_cs_sem3_notes,btech_cs_sem4_notes,btech_ce_sem8_notes,btech_ce_sem7_notes,btech_ce_sem6_notes,bca_sem1_notes,btech_ce_sem5_notes,btech_ce_sem4_notes,btech_ce_sem3_notes,btech_cs_sem8_notes,btech_cs_sem7_notes,btech_cs_sem6_notes,btech_cs_sem5_notes


# Create your views here.

def notes(request):
    return render (request, "notes/course.html")

def bca(request):
    return render (request, "notes/bca/sem.html")

def btech(request):
    return render (request, "notes/btech.html")

def mba(request):
    return render (request, "notes/mba/btech.html")


def btech_first(request):
    
    return render (request, "notes/btech/1st/sem.html")

def btech_first_sem1(request):
    btechsem1=btech_sem1_notes.objects.all()
    return render (request, "notes/btech/1st/sem1.html", {"btechsem1" :btechsem1} )

def btech_first_sem2(request):
    btechsem2=btech_sem2_notes.objects.all()
    return render (request, "notes/btech/1st/sem2.html", {"btechsem2" : btechsem2})

def btech_cs(request):
    return render (request, "notes/btech/cs/sem.html")

def btech_cs_sem1(request):
    btechcssem3=btech_cs_sem3_notes.objects.all()
    return render (request, "notes/btech/cs/sem1.html",{"btechcssem3":btechcssem3})

def btech_cs_sem2(request):
    btechcssem4=btech_cs_sem4_notes.objects.all()
    return render (request, "notes/btech/cs/sem2.html",{"btechcssem4":btechcssem4})

def btech_cs_sem3(request):
    btechcssem5=btech_cs_sem5_notes.objects.all()
    return render (request, "notes/btech/cs/sem3.html",{"btechcssem5":btechcssem5})

def btech_cs_sem4(request):
    btechcssem6=btech_cs_sem6_notes.objects.all()
    return render (request, "notes/btech/cs/sem4.html",{"btechcssem6":btechcssem6})

def btech_cs_sem5(request):
    btechcssem7=btech_cs_sem7_notes.objects.all()
    return render (request, "notes/btech/cs/sem5.html",{"btechcssem7":btechcssem7})

def btech_cs_sem6(request):
    btechcssem8=btech_cs_sem8_notes.objects.all()
    return render (request, "notes/btech/cs/sem6.html",{"btechcssem8":btechcssem8})

def btech_ce(request):
    
    return render (request, "notes/btech/ce/sem.html")

def btech_ce_sem1(request):
    btechcesem3=btech_ce_sem3_notes.objects.all()
    return render (request, "notes/btech/ce/sem1.html",{"btechcesem3":btechcesem3})

def btech_ce_sem2(request):
    btechcesem4=btech_ce_sem4_notes.objects.all()
    
    return render (request, "notes/btech/ce/sem2.html",{"btechcesem4":btechcesem4})

def btech_ce_sem3(request):
    btechcesem5=btech_ce_sem5_notes.objects.all()
    return render (request, "notes/btech/ce/sem3.html",{"btechcesem5":btechcesem5})

def btech_ce_sem4(request):
    btechcesem6=btech_ce_sem6_notes.objects.all()
    return render (request, "notes/btech/ce/sem4.html",{"btechcesem6":btechcesem6})

def btech_ce_sem5(request):
    btechcesem7=btech_ce_sem7_notes.objects.all()
    return render (request, "notes/btech/ce/sem5.html",{"btechcesem7":btechcesem7})

def btech_ce_sem6(request):
    btechcesem8=btech_ce_sem8_notes.objects.all()
    return render (request, "notes/btech/ce/sem6.html",{"btechcesem8":btechcesem8})

def btech_me(request):
    
    return render (request, "notes/btech/me/sem.html")

def btech_me_sem1(request):
    return render (request, "notes/btech/me/sem1.html")

def btech_me_sem2(request):
    return render (request, "notes/btech/me/sem2.html")

def btech_me_sem3(request):
    return render (request, "notes/btech/me/sem3.html")

def btech_me_sem4(request):
    return render (request, "notes/btech/me/sem4.html")

def btech_me_sem5(request):
    return render (request, "notes/btech/me/sem5.html")

def btech_me_sem6(request):
    return render (request, "notes/btech/me/sem6.html")

def btech_ec(request):
    return render (request, "notes/btech/ec/sem.html")

def btech_ec_sem1(request):
    return render (request, "notes/btech/ec/sem1.html")

def btech_ec_sem2(request):
    return render (request, "notes/btech/ec/sem2.html")

def btech_ec_sem3(request):
    return render (request, "notes/btech/ec/sem3.html")

def btech_ec_sem4(request):
    return render (request, "notes/btech/ec/sem4.html")

def btech_ec_sem5(request):
    return render (request, "notes/btech/ec/sem5.html")

def btech_ec_sem6(request):
    return render (request, "notes/btech/ec/sem6.html")

def btech_ee(request):
    return render (request, "notes/btech/ee/sem.html")

def btech_ee_sem1(request):
    return render (request, "notes/btech/ee/sem1.html")

def btech_ee_sem2(request):
    return render (request, "notes/btech/ee/sem2.html")

def btech_ee_sem3(request):
    return render (request, "notes/btech/ee/sem3.html")

def btech_ee_sem4(request):
    return render (request, "notes/btech/ee/sem4.html")

def btech_ee_sem5(request):
    return render (request, "notes/btech/ee/sem5.html")

def btech_ee_sem6(request):
    
    return render (request, "notes/btech/ee/sem6.html")


# bca notesjects & notes

def bca_sem(request):


    return render (request, "notes/bca/sem.html")

def bca_sem1(request):

    bcasem1=bca_sem1_notes.objects.all()

    return render (request, "notes/bca/sem1.html", {'bcasem1' : bcasem1})

def bca_sem2(request):
    bcasem2=bca_sem2_notes.objects.all()
    return render (request, "notes/bca/sem2.html", {'bcasem2' : bcasem2})

def bca_sem3(request):
    bcasem3=bca_sem3_notes.objects.all()
    return render (request, "notes/bca/sem3.html", {'bcasem3' : bcasem3})

def bca_sem4(request):
    bcasem4=bca_sem4_notes.objects.all()
    return render (request, "notes/bca/sem4.html", {'bcasem4' : bcasem4})

def bca_sem5(request):
    bcasem5=bca_sem5_notes.objects.all()
    return render (request, "notes/bca/sem5.html", {'bcasem5' : bcasem5})

def bca_sem6(request):
    bcasem6=bca_sem6_notes.objects.all()
    return render (request, "notes/bca/sem6.html", {'bcasem6' : bcasem6})

















