from django.shortcuts import render
from home.models import *

# Create your views here.
def admin_page(request):
    return render(request, 'admins/dashboard.html')

def bloglist(request):
    blog = Blog.objects.all()
    context = {
        'blog':blog
    }
    return render(request, 'admins/bloglist.html', context)