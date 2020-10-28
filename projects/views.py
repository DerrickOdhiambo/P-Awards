from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProfileSerializer, ProjectSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Project, Profile
from .forms import CreateUserForm, RatingForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
import requests
from django.template import loader


def index(request):
    images = Project.all_images()
    return render(request, 'projects/project_list.html', {'images': images})


class ProjectListView(ListView):
    model = Project
    context_object_name = 'images'


class UserProjectListView(ListView):
    model = Project
    template_name = 'auth/profile.html'
    context_object_name = 'images'

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(project_owner=user).order_by('-date_posted')


def view_project(request, pk):
    project = Project.get_image_by_id(id=pk)
    return render(request, 'projects/project_detail.html', {'project': project})


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'project_image', 'project_description', 'project_link']

    def form_valid(self, form):
        form.instance.project_owner = self.request.user
        return super().form_valid(form)


def Rate(request, project_id):
    project = Project.objects.get(id=project_id)
    user = request.user

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.project = project
            rate.save()
            return HttpResponseRedirect(reverse('project-detail', args=[project_id]))
    else:
        form = RatingForm()
    context = {
        'project': project,
        'form': form,
    }
    return render(request, 'projects/project_list.html', context)


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully!')
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'auth/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        user_update = UserUpdateForm(request.POST, instance=request.user)
        profile_update = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_update.is_valid() and profile_update.is_valid():
            user_update.save()
            profile_update.save()
            messages.success(
                request, f'Your account has been updated successfully!')
            return redirect('homepage')
    else:
        user_update = UserUpdateForm(instance=request.user)
        profile_update = ProfileUpdateForm()
    context = {
        'user_update': user_update,
        'profile_update': profile_update,
    }
    return render(request, 'auth/profile.html', context)


@api_view(['GET'])
def projectList(request):
    project = Project.objects.all()
    serializer = ProjectSerializer(project, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def projectDetail(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def profileList(request):
    profile = Profile.objects.all()
    serializer = ProjectSerializer(profile, many=True)
    return Response(serializer.data)


class SearchListView(ListView):
    model = User
    template_name = 'projects/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = self.request.GET.get('q')
        context['projects'] = Project.objects.filter(title__icontains=query)
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = User.objects.filter(username__icontains=query)
        return object_list


# used the api key to query from the database

def api_query(request):
    projects = requests.get(
        'https://awards26.herokuapp.com/api/project/').json()
    return render(request, 'projects/project_list.html', {'projects': projects})
