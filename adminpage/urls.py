from django.urls import path
from .views import *

urlpatterns = [
    path('', admin_page, name="adminpage"),
    path('bloglist', bloglist, name="bloglist"),
    path('addblog', addblog, name='addblog')
]