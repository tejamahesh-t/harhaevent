from django.shortcuts import render
from django.http import HttpResponse

# Create your views here

def index (request):
    return render(request,"index.html")

def about (request):
    return render(request,"about.html")

def blogsingle (request):
    return render(request,"blog-single.html")

def blog (request):
    return render(request,"blog.html")

def contact (request):
    return render(request,"contact.html")

def services (request):
    return render(request,"services.html")

def team (request):
    return render(request,"team.html")

def gallery(request):
    return render(request,"gallery.html")
    
def faqs(request):
    return render(request,"faqs.html")