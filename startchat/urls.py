from django.conf.urls import url,patterns
from startchat.views import *

urlpatterns = [
	url(r'^home/',homepage,name='home'),
	url(r'^upload/',listS,name='home'),
	url(r'^sign/',sign,name='sign'),
	url(r'^reigister/',Register,name='register'),
	url(r'^logined/',loginAcc,name='register'),
	url(r'^user_logout/',user_logout,name='user_logout'),
	url(r'^post/',your_post,name='your_post'),
	url(r'^searchuser/',searchUsers,name='searchUsers'),
	url(r'^profile/',profile,name='profile'),

	]