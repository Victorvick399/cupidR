from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url ,include
from . import views

urlpatterns=[
  url(r'^$',views.home,name='Home'),
  url(r'^profile/',views.profile,name='Profile'),
  url(r'^personal/profile/',views.my_profile,name='my_profile'),
  url(r'^update/profile/$',views.update_profile,name='Update_profile'),
  path('search/',views.search_user,name='search'),
  url(r'^new/post/$', views.post, name='post'),
  url(r'^p_search/$',views.profile_search,name='p_search'),
  path('user/profile/<user_name>/',views.other_user_profile,name="other_profile"), 
]
