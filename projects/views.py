from django.shortcuts import render
from projects.models import Project, Training

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project 
    }
    return render(request, "projects/project_detail.html", context)

def training_index(request):
    trainings = Training.objects.all()
    context = {
        "trainings": trainings
    }
    return render(request, "projects/training_index.html", context)

def training_detail(request, pk):
    training = Training.objects.get(pk=pk)
    context = {
        "training": training 
    }
    return render(request, "projects/training_detail.html", context)
