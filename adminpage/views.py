from django.shortcuts import render
from home.models import *
from django.core.paginator import Paginator

# Create your views here.
def admin_page(request):
    return render(request, 'admins/dashboard.html')

def bloglist(request):
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list, 20)  # Show 20 blogs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'admins/bloglist.html', context)