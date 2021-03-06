from django.shortcuts import render
from mywebsite.models import Message, Blog
from django.template.context_processors import csrf
from time import gmtime, strftime


def blog(request, post_name):
    try:
        post = Blog.objects.get(template_file=post_name)
        return render(request, "blog/" + post_name + '.html', {'post': post})
    except:
        context = {'message': "All blog posts don't exist!",
               "followup": "But these do -",
               'linkword': "blogs",
               "link": "/#blog"
               }

        return render(request, 'error.html', context)


def home(request):
    context = {}

    if 'submit' in request.POST:
        msg = Message(name=request.POST['name'], email=request.POST['email'],
                      message=request.POST['message'], subject=request.POST['subject'],
                      created=strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        msg.save()
        context.update({'message': 'Message Received!', 'messagetype': 'success'})

    context.update(csrf(request))
    return render(request, 'index.html', context)


def error(request):
    context = {'message': "Sorry, page not found!",
               "followup": "Let's take you ",
               'linkword': "home",
               "link": "/"
               }

    return render(request, 'error.html', context)


def sitemap(request):
    return render(request, 'sitemap.xml', {}, content_type='text/xml')