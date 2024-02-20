from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_short_story(request):
    return HttpResponse("Hello, Short Story!")
