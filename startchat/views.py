from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import cloudinary,cloudinary.uploader,cloudinary.api
from django.contrib import messages
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from startchat.forms import DocumentForm

# Create your views here.
@csrf_exempt
@login_required(login_url = '/sign')
def homepage(request):
	user = request.user
	picObject = MyPic.objects.all().order_by('-id')
	comments = CommentIs.objects.all()
	form = DocumentForm()
	return render(request,'index.html',{'user':user, 'comments':comments, 'form':form,'picObject':picObject})


@csrf_exempt
@login_required(login_url = '/sign')
def listS(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
    # Handle file upload
	if request.method == 'POST':
		data = request.POST
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = MyPic(image_is=request.FILES['docfile'])
			newdoc.uploadBy = myuserObject

			newdoc.image_caption = data['caption'].capitalize()
			newdoc.save()
			print('image has been uploaded!!!')

            # Redirect to the document list after POST
			return redirect('/home/')
	else:
		form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    # documents = Document.objects.all()

    # Render list page with the documents and the form
	return render(request,'index.html',{'myuserObject': myuserObject, 'form': form})


def sign(request):
	return render(request,'login.html')


def Register(request):
	if request.method == 'POST':
		form = request.POST

		try:
			userFilter = User.objects.get(username = form['email'])
			messages.warning(request,'You are already Registered!!!')
			return redirect('/sign/')

		except:

			email = form['email']
			password = form['password']

			user = User.objects.create_user(
				username = email,
				password = password

				)
			myUser = MyUser.objects.create(
				email = email,
				user = user

				)
			messages.warning(request,'You are Registered!!!')
			return redirect('/sign/')



@csrf_exempt
def loginAcc(request):
	
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
	if user is not None:
		if user.is_active:
			try:
				login(request, user)
				
				first_name = user.first_name
				# emailReq = user.username

				userObject = MyUser.objects.get(user = user)
				userObject.is_loggedIn = True
				userObject.last_logged_in = datetime.now()
				userObject.save()
			except:
				messages.warning(request,"This account is not found!!")
				return render(request,'login.html')
			
			return redirect('/home/')
		else:
			print(3)
			messages.warning(request,"This account is not activated!!")
			return render(request,'login.html')

	else:
		print(4)
		messages.warning(request," Enter Correct username and password!!")
		return render(request,'login.html')


@csrf_exempt
@login_required(login_url='/sign')
def user_logout(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)
	myuserObject.is_loggedIn = False
	myuserObject.save()
	logout(request)
	messages.warning(request,'You are logged out!!!!')
	return redirect('/sign/')

@csrf_exempt
@login_required(login_url = '/sign')
def your_post(request):
	user = request.user
	myuserObject = MyUser.objects.get(user = user)

	if request.method == 'POST':
		form = request.POST


		post_is = form['post']

		myPic = MyPic.objects.create(
			uploadBy = myuserObject,
			image_caption = post_is,
			)

		return redirect('/home/')
	else:
		return redirect('/home/')

@csrf_exempt
@login_required(login_url = '/sign')
def searchUsers(request):
	if request.method == 'POST':
		form = request.POST
		user = request.user
		myuserObject = MyUser.objects.get(user = user)

		search = form['search']

		try:
			userObject = User.objects.get(username = search)
			myuserObjectSearched = MyUser.objects.get(user = userObject)
			try:
				profilePic = MyProfilePic.objects.get(uploadBy = myuserObjectSearched)
				return render(request,'search.html',{'profilePic':profilePic, 'myuserObjectSearched':myuserObjectSearched})
			except:
				return render(request,'search.html',{'myuserObjectSearched':myuserObjectSearched})

		except:
			messages.warning(request,'No users Found!!!')
			return redirect('/home/')

@csrf_exempt
@login_required(login_url = '/sign')
def profile(request):
	return render(request,'search.html')