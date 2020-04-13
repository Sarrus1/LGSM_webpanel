from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from .forms import NewServerForm
from django.contrib.auth.decorators import login_required

@login_required
def newserver(request):
    if request.method == 'POST':
        form = NewServerForm(request.POST)
        if form.is_valid():
            form.save()
            servername = form.cleaned_data.get('Name')
            messages.success(request, f'{servername} was succesfuly added!')
            return redirect('webpanel-index')
    else:
        form = NewServerForm()
    return render(request, 'servers/newserverform.html', {'form': form})
