from django.shortcuts import render
#this is for forms for registratio (authentication)
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


# Create your views here.
from django.http import HttpResponse

def world(request):
    context ={'mytext' : "hey everyone"}

    return render(request, 'polls/hello_world.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            
            
            form.save()
            return render(request, 'polls/register.html', {'form': CustomUserCreationForm(), 'message': 'Registration successful!'})
            # return redirect('login')  # Redirect to login page after registration
        else:
            return render(request, 'polls/register.html', {'form': form, 'message': 'Registration failed. Please correct the errors below.'})
    else:
        form = CustomUserCreationForm()
    return render(request, 'polls/register.html', {'form': form, 'message': ''})