from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from app.choices import GENDER_CHOICES, COMPLEXION_CHOICES, PERSONALITY_CHOICES, HEIGHT_CHOICES, AGE_CHOICES

# Create your models here.


class Profile(models.Model):
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    profile_pic = ImageField(blank=True, manual_crop='')
    bio = models.TextField(max_length=300)
    age = models.IntegerField(choices=AGE_CHOICES, default=0)
    complexion = models.IntegerField(choices=COMPLEXION_CHOICES, default=0)
    personality = models.IntegerField(choices=PERSONALITY_CHOICES, default=0)
    height = models.IntegerField(choices=HEIGHT_CHOICES, default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio


class Preference(models.Model):
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.IntegerField(choices=AGE_CHOICES)
    complexion = models.IntegerField(choices=COMPLEXION_CHOICES)
    personality = models.IntegerField(choices=PERSONALITY_CHOICES)
    height = models.IntegerField(choices=HEIGHT_CHOICES)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.gender


class Post(models.Model):
    image = ImageField(blank=True, manual_crop='')
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name