from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def world(request):
    context ={'mytext' : ""}

    return render(request, 'polls/hello_world.html', context)
