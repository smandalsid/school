# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Subject, Quiz, Student, Question

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    
admin.site.register(User, CustomUserAdmin)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Question)