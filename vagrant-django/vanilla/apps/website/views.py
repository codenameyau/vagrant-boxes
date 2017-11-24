"""
Application: website

Contains the views for static websites. You should put static content
like the 'About' page here.
"""
from django.shortcuts import render

def home(request):
    """
    Default homepage for the django-vagrant-box project.
    Feel free to delete this view when it's no longer needed.
    """
    return render(request, 'index.html')
