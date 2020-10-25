from django.shortcuts import render
from .models import Project


def index(request):
    images = Project.all_images()
    return render(request, 'projects/index.html', {'images': images})
