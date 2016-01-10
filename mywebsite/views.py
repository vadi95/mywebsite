from django.shortcuts import render
from mywebsite.models import Message
from django.template.context_processors import csrf

def home(request):
    context = {}

    if 'submit' in request.POST:
        msg = Message(name=request.POST['name'], email=request.POST['email'],
                    message=request.POST['message'])
        msg.save()
        context.update({'message': 'Message Received!', 'messagetype': 'success'})

    context.update(csrf(request))
    return render(request, 'index.html', context)

def blog(request):
    return render(request, 'blog.html')

def error(request):
    return render(request, 'error.html')
