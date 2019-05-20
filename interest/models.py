from djongo import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# class leta(models.Model):
# 	"""docstring for leta"""
# 	pubg_date=models.DateField()
# 	class Meta:
# 		abstract=True			


# class deta(models.Model):
# 	name=models.CharField(max_length=100)
# 	tagline=models.TextField()
# 	img=models.ImageField(upload_to="photodir", blank=True)
# 	def __str__(self):
# 		return self.name		

# 	class Meta:
# 		abstract = False

# class feta(models.Model):
# 	letaa=models.EmbeddedModelField(model_container=leta,)

# 	name=models.CharField(max_length=100)

tag_ch=(('events','Events'),('photography','Photography'),('family','Family'),('friends','Friends'))

class PicPost(models.Model):
	title = models.CharField(max_length=50)
	content = models.CharField(max_length=200)
	date_posted = models.DateTimeField(default=timezone.now)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	tags=models.CharField(max_length=20,choices=tag_ch,default='Events')
	image=models.ImageField(default='default.jpeg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.title} PicPost'

	def get_absolute_url(self):
		return reverse('home',kwargs={})	

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

class PicProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	title=models.CharField(max_length=20)
	date_posted= models.DateTimeField(default=timezone.now)
	content=models.CharField(max_length=200)
	tags=models.CharField(max_length=20,choices=tag_ch,default='Events')
	image=models.ImageField(default='default.jpeg', upload_to='new1')


	def __str__(self):
		return f'{self.user.username} PicProfile'		
