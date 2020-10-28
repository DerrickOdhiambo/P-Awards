from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import ProjectListView, ProjectCreateView, UserProjectListView, SearchListView
from . import views


urlpatterns = [
    path('', ProjectListView.as_view(), name='homepage'),
    path('user/<str:username>/', UserProjectListView.as_view(), name='user-projects'),
    path('project/<int:pk>/', views.view_project, name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('search/',  SearchListView.as_view(), name='search-users'),
    path('api/project/', views.projectList, name='project-list'),
    path('api/profile/', views.projectList, name='profile-list'),
    # path('', views.api_query, name='homepage')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
