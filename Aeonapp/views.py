from django.shortcuts import render
from Aeonapp.models import *
def home(request):
    return render(request,'home1.html')

def trainingandIntern1(request):
    return render(request,'training&internship1.html')

def trainingandIntern2(request):
    return render(request,'training&internship2.html')  

def trainingform(request):
    b={}
    a={}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profession = request.POST.get('profession')
        institute = request.POST.get('institute')
        state = request.POST.get('state')
        queries = request.POST.get('queries')
        if username == '' or email == '' or phone == '' or profession == '' or institute == '' or state == '':
            b['err']="field is empty"
            return render(request, 'trainingform.html',b)
        else:
            a= WorkshopFormDetails.objects.create(
            username=username,
            email=email,
            phone=phone,
            profession=profession,
            institute=institute,
            state=state,
            queries=queries
        )
        a.save()
        b['success']="you'r applied is successfully"
        return render(request, 'train.html',b)
    else:
        return render(request,'trainingform.html')

def workshop(request):
    a={}
    w=WorkshopDetail.objects.filter(is_active=True)
    a['desc']=w
    return render(request,'workshoppg.html',a)  

def workshopform(request):
    b={}
    a={}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profession = request.POST.get('profession')
        institute = request.POST.get('institute')
        state = request.POST.get('state')
        queries = request.POST.get('queries')
        if username == '' or email == '' or phone == '' or profession == '' or institute == '' or state == '':
            b['err']="field is empty"
            return render(request, 'workshopform.html',b)
        else:
            a= WorkshopFormDetails.objects.create(
            username=username,
            email=email,
            phone=phone,
            profession=profession,
            institute=institute,
            state=state,
            queries=queries
        )
        a.save()
        b['success']="you'r applied is successfully"
        return render(request, 'workshopform.html',b)
    else:
        return render(request,'workshopform.html')

def research_papers(request):
    papers_by_range = {}
    for paper in PublicationPaper.objects.all().order_by('year', 'title'):
        start_year = (paper.year // 5) * 5
        end_year = start_year + 4
        range_key = f"{start_year}-{end_year}"
        if range_key not in papers_by_range:
            papers_by_range[range_key] = {}
        if paper.year not in papers_by_range[range_key]:
            papers_by_range[range_key][paper.year] = []
        papers_by_range[range_key][paper.year].append(paper)

    context = {
        'papers_by_range': papers_by_range,
    }
    return render(request, 'publication.html', context)

def publicationform(request):
    b = {}
    a={}
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        profession=request.POST.get('profession')
        institute=request.POST.get('institute')
        state=request.POST.get('state')
        queries=request.POST.get('queries')
        if username == '' or email == '' or phone == '' or profession == '' or institute == '' or state == '':
            b['err']="field is empty"
            return render(request,'publication.html',b)
        else:
            a=PublicationFormDetail.objects.create(
                username=username,
                email=email,
                phone=phone,
                profession=profession,
                institute=institute,
                state=state,
                queries=queries)
            a.save()
            b['success']="you'r applied is successfully"
            return render(request,'publicationform.html',b)
    else:
        return render(request,'publicationform.html')

def manuscript(request):
    b = {}
    a={}
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        profession=request.POST.get('profession')
        institute=request.POST.get('institute')
        state=request.POST.get('state')
        queries=request.POST.get('queries')
        if username == '' or email == '' or phone == '' or profession == '' or institute == '' or state == '':
            b['err']="field is empty"
            return render(request,'manuscript.html',b)
        else:
            a=ManuscriptFormDetail.objects.create(
                username=username,
                email=email,
                phone=phone,
                profession=profession,
                institute=institute,
                state=state,
                queries=queries)
            a.save()
            b['success']="you'r applied is successfully"
            return render(request,'manuscript.html',b)
    else:
        return render(request,'manuscript.html')
    

def contactus(request):
    b={}
    a={}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profession = request.POST.get('profession')
        institute = request.POST.get('institute')
        state = request.POST.get('state')
        queries = request.POST.get('queries')
        if username == '' or email == '' or phone == '' or profession == '' or institute == '' or state == '':
            b['err']="field is empty"
            return render(request, 'contactus.html',b)
        else:
            a= ContactusFormDetails.objects.create(
            username=username,
            email=email,
            phone=phone,
            profession=profession,
            institute=institute,
            state=state,
            queries=queries
        )
        a.save()
        b['success']="you'r applied is successfully"
        return render(request, 'contactus.html',b)
    else:
        return render(request,'contactus.html')
    

def aboutus(request):
    return render(request,'aboutus.html')


