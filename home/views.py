from django.shortcuts import render
from . models import *

# Create your views here.
def homepage(request):
    recent_blog = Blog.objects.all().order_by('-id')[:1]
    blogs = Blog.objects.all()
    context = {
        'recent':recent_blog,
        'blogs':blogs
    }
    return render(request, 'home/index.html', context)