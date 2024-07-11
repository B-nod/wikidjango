from django.shortcuts import render
from home.models import *
from django.core.paginator import Paginator

# Create your views here.
def admin_page(request):
    return render(request, 'admins/dashboard.html')

def bloglist(request):
    blog = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog, 10)
    page_number = request.GET.get(page_number)
    page_obj = paginator.get_page(page_number)
    page_range = range(1, paginator.num_pages +1)
    context = {
        'blog':blog,
        'page_obj':page_obj,
        'page_range':page_range
    }
    return render(request, 'admins/bloglist.html', context)