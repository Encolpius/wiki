from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from saltmarsh.models import Comment

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome to Saltmarsh, {username}. You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    comments = Comment.objects.all().order_by("-date_posted")[:5]
    return render(request, "users/profile.html", { "comments": comments })

@login_required
def profile_update(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'p_form': p_form
    }
    return render(request, "users/profile_update.html", context)

def show_user_profile(request, username):
    comments = Comment.objects.all().order_by("-date_posted")[:5]
    user = User.objects.get(username__icontains=username)
    return render(request, 'users/profile_detail.html', {'user': user, 'comments': comments})