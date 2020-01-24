from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from app.forms import PreferenceForm, ProfileForm, PostForm
from app.models import Preference, Profile, Post
from django.contrib.auth import logout
from django.db.models import Q
from allauth.account.decorators import verified_email_required

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        matches = Profile.objects.filter(~Q(gender=request.user.profile.gender)).all()
        for match in matches:
            users = User.objects.filter(id=match.user.id).all()
            print(users)
        return render(request, 'profile.html',{"users":users})
    else:
        return render(request, 'home.html')


@login_required(login_url='/accounts/login/')
def profile(request):
    """
     View function that returns profile page
    """
    current_user = request.user
    if current_user.profile is None:
        users = User.objects.all()
    else:
        matches = Profile.objects.filter(
            ~Q(gender=request.user.profile.gender)).all()
        print(matches)
        for match in matches:
            users = User.objects.filter(id=match.user.id).all()
            print(users)
    return render(request, 'profile.html', {"users": users})

@login_required(login_url='/accounts/login/')
def my_profile(request):
    '''
    view function to view personal profile
    '''
    current_user=request.user
    form = PostForm()
    title = request.user.username
    posts = Post.objects.filter(user=request.user.id)
   
    context = {
        'title': title,
        'posts': posts,
        'form':form,
    }
    return render(request, 'pers_profile.html', context)


@login_required(login_url='/accounts/login')
def profile_search(request):
    current_user = request.user
    form = PreferenceForm()

    return render(request, 'search.html', {"form": form})


@login_required(login_url='accounts/login')
def update_profile(request):
    '''
    Function that renders the update profile template and passes the form into it.
    '''
    current_user = request.user
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            Profile.objects.filter(user_id=current_user.id).delete()
            profile = profile_form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect("Profile")
    else:
        profile_form = ProfileForm()

    return render(request, 'updateprofile.html', {"profile_form": profile_form})


@login_required(login_url='/accounts/login')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()

    posts = Post.objects.filter(user=request.user.id)

    return render(request, 'pers_profile.html', {"form": form,"posts":posts})


@login_required()
def other_user_profile(request, user_name):
    '''
    view function that renders the profile for other users
    '''
    title = user_name
    other_user = User.objects.get(username=user_name)
    posts = Post.objects.filter(user=other_user)
    context = {
        'title': title,
        'other_user': other_user,
        'posts': posts,
    }
    return render(request, 'other_profile.html', context)


@login_required(login_url='accounts/login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('Home')


@login_required(login_url='/accounts/login/')
def search_user(request):
    current_user = request.user
    form = PreferenceForm()
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            g = request.POST['gender']
            c = request.POST['complexion']
            p = request.POST['personality']
            matches = Profile.objects.filter(
                gender=g, complexion=c, personality=p).all()
            for match in matches:
                p_users = User.objects.filter(id=match.user.id).all()

    return render(request, 'search.html', {"users": p_users, "form": form})
