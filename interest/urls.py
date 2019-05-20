"""big_data_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView,PostCreateView
from django.conf import settings
from django.conf.urls.static import static

# app_name="interest"

urlpatterns = [
	path('home',views.home,name='home'),
    # path('',PostListView.as_view() ,name='home'),
	path('post/new/',PostCreateView.as_view() ,name='picpost-create'),
    path("about",views.about,name="about"),
    path("ourstory",views.ourstory,name="ourstory"),
    path("gallery",views.gallery,name="gallery"),
    path("upl_post",views.upl_post,name="upl_post"),
    # path('admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)