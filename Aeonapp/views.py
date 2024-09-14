from django.shortcuts import render
from Aeonapp.models import WorkshopDetail
def home(request):
    return render(request,'home1.html')

def trainingandIntern1(request):
    return render(request,'training&internship1.html')

def trainingandIntern2(request):
    return render(request,'training&internship2.html')  

def trainingform(request):
    return render(request,'trainingform.html')

def workshop(request):
    a={}
    w=WorkshopDetail.objects.filter(is_active=True)
    a['desc']=w
    return render(request,'workshoppg.html',a)

def workshopform(request):
    
    return render(request,'workshopform.html')

def publication(request):
    return render(request,'publication.html')

def publicationform(request):
    return render(request,'publicationform.html')

def manuscript(request):
    return render(request,'manuscript.html')

