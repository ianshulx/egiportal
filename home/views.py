from django.shortcuts import render
from django.http import HttpRequest
from django.http import request
from django.contrib.auth.decorators import login_required
from home.models import notice1, quiz, book, image, notice,event1, Main_Event

# Create your views here.
# def main(request):
#     return render(request, 'main.html')
@login_required   
def frequently(request):
    return render(request, 'frequently.html')
@login_required
def hod(request):
    return render(request, 'hod.html')
@login_required
def sources(request):
    return render(request, 'Sources.html')
@login_required
def team(request):
    return render(request, 'team.html')
@login_required
def contact(request):
    return render(request, 'contact.html')

@login_required
def notice(request):
    notices=notice1.objects.all()
    return render(request, 'Notice.html', {'notices':notices})

@login_required
def event(request):
    events=event1.objects.all()
    
    return render(request, 'events.html', {'events':events})


@login_required
def quize(request):
    quizes=quiz.objects.all()
    return render(request, 'quizes.html', {'quizes':quizes})

@login_required
def library(request):
    books=book.objects.all()
    return render(request, 'library.html', {'books':books})

@login_required
def gallary(request):
    images=image.objects.all()
    return render(request, 'gallary.html', {'images':images})

@login_required
def not_available(request):
    return render(request, 'not.html' )

@login_required
def not_available2(request):
    return render(request, 'not2.html' )
