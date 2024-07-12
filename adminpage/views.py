from django.shortcuts import render, redirect
from home.models import *
from home.forms import *
from django.core.paginator import Paginator
from django.contrib import messages

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

def addblog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Blog added successfully')
            return redirect('/wikiadmin/addblog')
        else:
            messages.add_message(request, messages.ERROR, 'Kindly verify all the fields')
            return render(request, 'admins/addblog.html', {'form':form})
    
    context = {
        'form':BlogForm
    }
    return render(request,'admins/addblog.html', context)