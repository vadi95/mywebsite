from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def error(request):
    return render(request, 'error.html')