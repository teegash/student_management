from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from student_management_app.models import CustomUser


# Register your models here.
#Creating Blank UserModel Class and Registering into admin.py
#If i don't create Blank UserModel Then password will not be Encrypted
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)
