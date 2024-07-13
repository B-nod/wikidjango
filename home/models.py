# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adds(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    filename = models.TextField()
    url = models.TextField()
    adcode = models.TextField()
    indexing = models.IntegerField()
    type = models.TextField()
    position = models.TextField()
    ondate = models.DateField(db_column='onDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adds'

class Cities(models.Model):
    title = models.CharField(max_length=250)
    category_title = models.CharField(max_length=250)
    pagetitle = models.TextField()
    pagekeyword = models.TextField()
    pagedescription = models.TextField()
    weight = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'cities'


class Blog(models.Model):
    blog_title = models.TextField()
    urltitle = models.CharField(max_length=250)
    blog_author = models.TextField()
    date_of_birth = models.DateField()
    networth = models.TextField()
    height = models.TextField()
    married = models.TextField()
    blog_description = models.TextField()
    blog_published_date = models.DateTimeField(db_column='blog_published_Date')  # Field name made lowercase.
    filename = models.TextField()
    categories = models.ForeignKey(Cities, on_delete=models.CASCADE)
    pagetitle = models.TextField(db_column='pageTitle')  # Field name made lowercase.
    visitor = models.IntegerField()
    metakeyword = models.TextField(db_column='metaKeyword')  # Field name made lowercase.
    metadescription = models.TextField(db_column='metaDescription')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'blog'




class Comment(models.Model):
    id = models.FloatField(primary_key=True)
    name = models.TextField()
    address = models.TextField()
    email = models.TextField()
    comment = models.TextField()
    commnet_published_date = models.DateField()
    article_id = models.FloatField()
    main = models.IntegerField()
    res_id = models.IntegerField()
    publish = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'comment'


class Galleries(models.Model):
    groupid = models.IntegerField(db_column='groupId')  # Field name made lowercase.
    caption = models.TextField()
    ext = models.TextField()
    ondate = models.DateField(db_column='onDate')  # Field name made lowercase.
    pagetitle = models.CharField(db_column='pageTitle', max_length=250)  # Field name made lowercase.
    pagekeyword = models.CharField(db_column='pageKeyword', max_length=250)  # Field name made lowercase.
    imagelink = models.CharField(db_column='imageLink', max_length=100)  # Field name made lowercase.
    imageposition = models.TextField(db_column='imagePosition')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'galleries'


class Groups(models.Model):
    name = models.CharField(max_length=200)
    urlname = models.CharField(max_length=250)
    days = models.CharField(max_length=20)
    grading = models.CharField(max_length=100)
    altitudename = models.CharField(db_column='altitudeName', max_length=100)  # Field name made lowercase.
    altitudeheight = models.IntegerField(db_column='altitudeHeight', db_comment='height in meters')  # Field name made lowercase.
    tripdeparturename = models.CharField(db_column='tripDepartureName', max_length=100)  # Field name made lowercase.
    costamount = models.IntegerField(db_column='costAmount', db_comment='amount in USD')  # Field name made lowercase.
    type = models.CharField(max_length=200)
    parentid = models.IntegerField(db_column='parentId')  # Field name made lowercase.
    shortcontents = models.TextField()
    contents = models.TextField()
    overview = models.TextField(blank=True, null=True)
    videourl = models.TextField(db_column='videoUrl')  # Field name made lowercase.
    destination_show = models.CharField(max_length=250)
    triphightlight = models.TextField()
    faq_details = models.TextField()
    itinerary = models.TextField(blank=True, null=True)
    contentlink = models.TextField(db_column='contentLink', blank=True, null=True)  # Field name made lowercase.
    image_title = models.TextField()
    image_alt = models.TextField()
    tripseasons = models.TextField(db_column='tripSeasons', blank=True, null=True)  # Field name made lowercase.
    tripcode = models.TextField(db_column='tripCode', blank=True, null=True)  # Field name made lowercase.
    triprating = models.TextField(db_column='tripRating', blank=True, null=True)  # Field name made lowercase.
    mountain = models.TextField(blank=True, null=True)
    destination = models.TextField(blank=True, null=True)
    routemap = models.TextField()
    contents_spring = models.TextField(blank=True, null=True)
    linktype = models.CharField(db_column='linkType', max_length=255)  # Field name made lowercase.
    weight = models.IntegerField()
    act = models.IntegerField()
    popular = models.CharField(max_length=250)
    special = models.CharField(max_length=250)
    ondate = models.DateField(db_column='onDate')  # Field name made lowercase.
    ext = models.TextField()
    extt = models.CharField(max_length=10)
    hide = models.CharField(max_length=3)
    pagetitle = models.CharField(db_column='pageTitle', max_length=250)  # Field name made lowercase.
    pagekeyword = models.CharField(db_column='pageKeyword', max_length=250)  # Field name made lowercase.
    metadescription = models.TextField(db_column='metaDescription')  # Field name made lowercase.
    visits = models.IntegerField()
    enquiry_button_status = models.IntegerField()
    trip_code = models.CharField(max_length=250)
    special_trekking_packages = models.CharField(max_length=250)
    special_tour_packages = models.CharField(max_length=250)
    special_climbing_packages = models.CharField(max_length=250)
    featured_trip = models.CharField(max_length=250)
    best_selling_trip = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'groups'


class Linkexchange(models.Model):
    fullname = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fileimage = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    ondate = models.DateTimeField(db_column='onDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'linkexchange'


class Metahome(models.Model):
    pagetitle = models.TextField(db_column='pageTitle', blank=True, null=True)  # Field name made lowercase.
    pagekeyword = models.TextField(db_column='pageKeyword', blank=True, null=True)  # Field name made lowercase.
    metadescription = models.TextField(db_column='metaDescription', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'metahome'


class Testimonials(models.Model):
    test_id = models.IntegerField()
    name = models.CharField(db_column='Name', max_length=250)  # Field name made lowercase.
    address = models.CharField(max_length=250)
    comments = models.TextField(db_column='Comments')  # Field name made lowercase.
    filename = models.CharField(max_length=250)
    status = models.IntegerField()
    ndate = models.DateField(db_column='nDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'testimonials'


class Usergroups(models.Model):
    name = models.CharField(max_length=200)
    power = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usergroups'


class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    lastlogin = models.DateTimeField(db_column='lastLogin')  # Field name made lowercase.
    logintimes = models.PositiveIntegerField(db_column='loginTimes')  # Field name made lowercase.
    status = models.CharField(max_length=1)
    usergroupid = models.PositiveIntegerField(db_column='userGroupId')  # Field name made lowercase.
    email = models.TextField()

    class Meta:
        managed = False
        db_table = 'users'


class Videos(models.Model):
    groupid = models.PositiveIntegerField(db_column='groupId')  # Field name made lowercase.
    title = models.TextField()
    url = models.CharField(max_length=100)
    ondate = models.DateField(db_column='onDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'videos'
