from django.contrib import admin
from app.models import Profile,Preference

# Register your models here.
admin.site.register(Preference)
admin.site.register(Profile)