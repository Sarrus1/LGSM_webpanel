from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def logout_views(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

