from django.forms import ModelForm
from . models import *

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

class AdsForm(ModelForm):
    class Meta:
        model = Adds
        fields = "__all__"

class CitiesForm(ModelForm):
    class Meta:
        model = Cities
        fields = "__all__"

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"

class GalleiresForm(ModelForm):
    class Meta:
        model = Galleries
        fields = "__all__"


class GroupsForm(ModelForm):
    class Meta:
        model = Groups
        fields = "__all__"


class LinkexchangeForm(ModelForm):
    class Meta:
        model = Linkexchange
        fields = "__all__"

class MetahomeForm(ModelForm):
    class Meta:
        model = Metahome
        fields = "__all__"


class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonials
        fields = "__all__"

class UsergroupsFrom(ModelForm):
    class Meta:
        model = Usergroups
        fields = "__all__"

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = "__all__"


class VideosForm(ModelForm):
    class Meta:
        model = Videos
        fields = "__all__"