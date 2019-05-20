from django.contrib import admin
from interest.models import Profile,PicPost,PicProfile

# Register your models here.

admin.site.register([Profile,PicPost,PicProfile])