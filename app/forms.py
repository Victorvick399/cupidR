from django import forms
from .models import Profile, Preference, Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import LoginForm, SignupForm

class ProfileForm(forms.ModelForm):
    '''
    class that defines how the update profile form will look like
    '''
    class Meta:
        model = Profile
        fields=['profile_pic','bio','gender','age','complexion','personality','height']
        exclude = ['user']

class PreferenceForm(forms.ModelForm):
    '''
    class that defines how to search for prefernce
    '''
    class Meta:
        model = Profile
        fields=['gender','age','complexion','personality']
        exclude = ['user_id']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','name']


class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)

class MyCustomSignupForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user

