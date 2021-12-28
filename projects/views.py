from django.shortcuts import render
from django.http import HttpRequest
from django.http import request
from django.contrib.auth.decorators import login_required
from .models import project
from .form import projectform


# Create your views here.
@login_required
def projects(request):
    
    if request.method=="POST":
        form=projectform(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save() 
            obj=form.instance
            return render(request, 'projects/Projects.html', {"obj": obj})
    else:
        form=projectform()
        Allprojects=project.objects.all()
        
    return render(request, 'projects/Projects.html', {'Allprojects': Allprojects})
