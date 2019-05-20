from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from django.views.generic import ListView,CreateView
import pickle
import json
from .models import Profile,PicPost
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from .models import PicPost


# Create your views here.

posts=[{
	'author':'rana',
	'title':'post1',
	'content':'hahahah',
},
{
	'author':'rauff',
	'title':'post2',
	'content':'nananan',
},

]


@login_required
@csrf_exempt
def home(request):
	posts=PicPost.objects.all()
	return render(request=request,template_name="index.html", context={"posts":posts})


class PostListView(ListView):
	model = PicPost
	template_name='index.html'
	context_object_name='posts'

class PostCreateView(CreateView):
	model = PicPost
	fields = ['title','content','tags','image']
	template_name="picpost_form.html"

	def form_valid(self, form):
		form.instance.owner=self.request.user
		return super().form_valid(form)

@login_required
def ourstory(request):
	posts=PicPost.objects.all()
	return render(request=request,template_name="ourstory.html",context={"posts":posts})


@login_required
def gallery(request):
	posts=PicPost.objects.all()
	return render(request=request, template_name="gallery.html", context={"posts":posts})

def about(request):
		return render(request=request, template_name="about.html")
@login_required
def upl_post(request):
	print(PicPost)

	return render(request=request,template_name="events.html",context={})			