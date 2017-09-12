from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.

class CountryMaster(models.Model):
	name = models.CharField(max_length = 100,null = True,blank = True)
	last_modifiedBy = models.CharField(max_length = 100,null = True, blank = True)
	last_modified_DateTime = models.DateTimeField(null = True,blank = True)

	def __str__(self):
		return '%s' % (self.name)

class StateMaster(models.Model):
	name = models.CharField(max_length = 100,null = True,blank = True)
	countryId = models.ForeignKey(CountryMaster,null = True,blank = True)
	last_modifiedBy = models.CharField(max_length = 100,null = True, blank = True)
	last_modified_DateTime = models.DateTimeField(null = True,blank = True)

	def __str__(self):
		return '%s' % (self.name)

class CityMaster(models.Model):
	name = models.CharField(max_length = 100,null = True,blank = True)
	stateId = models.ForeignKey(StateMaster,null = True,blank = True)
	last_modifiedBy = models.CharField(max_length = 100,null = True, blank = True)
	last_modified_DateTime = models.DateTimeField(null = True,blank = True)

	def __str__(self):
		return '%s' % (self.name)


class MyUser(models.Model):
	user = models.OneToOneField(User,null = True, blank = True)
	email = models.EmailField(unique = True, null = True, blank = True)
	gender = models.CharField(max_length = 300,null = True, blank = True)
	country = models.ForeignKey(CountryMaster,null = True,blank = True)
	state = models.ForeignKey(StateMaster,null = True,blank = True)
	city = models.ForeignKey(CityMaster,null = True,blank = True)
	mobileNumber = models.BigIntegerField(null = True, blank = True)
	full_address = models.CharField(max_length = 300,null = True, blank = True)
	pincode = models.IntegerField(null = True,blank = True)
	isProfileComplete = models.BooleanField(default = False)
	is_activeYesNO = models.BooleanField(default = False)
	is_loggedIn = models.BooleanField(default = False)
	last_logged_in = models.DateTimeField(null = True, blank = True)
	created_date_time = models.DateTimeField(null = True, blank = True)
	def __str__(self):
		return '%s %s' % (self.user.username,self.mobileNumber)

class MyPic(models.Model):
	uploadBy = models.ForeignKey(MyUser,null = True, blank = True)
	image_is = models.ImageField(upload_to = 'profile_image',blank = True,null = True)
	imageUrl = models.URLField(null = True, blank = True)
	image_caption = models.CharField(max_length = 300,null = True,blank = True)
	uploadedOn = models.DateField(auto_now_add = True,null = True,blank = True)
	uploadedTim = models.TimeField(auto_now_add = True,null = True,blank = True)

	def __str__(self):
		return '%s' % (self.id)

class CommentIs(models.Model):
	commentBy = models.ForeignKey(MyUser,null = True, blank = True)
	commentedImage = models.ForeignKey(MyPic,null = True,blank = True)
	comment_is = models.TextField(null = True, blank = True)
	commentOn = models.DateField(auto_now_add = True,null = True,blank = True)
	commentTim = models.TimeField(auto_now_add = True,null = True,blank = True)

class MyProfilePic(models.Model):
	uploadBy = models.OneToOneField(MyUser,null = True, blank = True)
	image_is = models.ImageField(upload_to = 'profile_image',blank = True,null = True)
	uploadedOn = models.DateField(auto_now_add = True,null = True,blank = True)
	uploadedTim = models.TimeField(auto_now_add = True,null = True,blank = True)

	def __str__(self):
		return '%s' % (self.id)


class MyFriendRequest(models.Model):
	UserId = models.ForeignKey(MyUser,null = True, blank = True)
	FriendId = models.ForeignKey(MyUser,related_name = 'friend',null = True, blank = True)
	requestSentDateTime = models.DateTimeField(auto_now_add = True,null = True, blank = True)