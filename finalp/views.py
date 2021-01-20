from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import user
from django.db import connections
def home(request):
    return render(request,'bs.html')

# Create your views here.
def owasp_homepage(request):
    return render(request,'owasp_homepage.html')

def one(request):
    return render(request,'one.html')

def two(request):
    return render(request,'two.html')

def three(request):
    return render(request,'three.html')

def four(request):
    return render(request,'four.html')

def five(request):
    return render(request,'five.html')

def six(request):
    return render(request,'six.html')

def seven(request):
    return render(request,'seven.html')

def eight(request):
    return render(request,'eight.html')

def nine(request):
    return render(request,'nine.html')

def ten(request):
    return render(request,'ten.html')

def netizens(request):
    return render(request,'netizens.html')

def form(request):
    un = request.GET.get('username')
    pwd = request.GET.get('password')
    ans = user.objects.raw("SELECT * FROM finalp_user where user_name='{}'".format(un))
    #with connection.cursor() as cursor:
         #cursor.execute("SELECT * from user where username='%s'",[self.un])
         #ans=cursor.fetchall()
    return render(request,'form.html',{'ans':ans})
