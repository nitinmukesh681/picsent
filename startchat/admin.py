from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CountryMaster)
admin.site.register(StateMaster)
admin.site.register(CityMaster)
admin.site.register(MyUser)
admin.site.register(MyPic)
admin.site.register(CommentIs)
admin.site.register(MyProfilePic)