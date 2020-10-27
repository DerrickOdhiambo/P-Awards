from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, UserProjectListView, SearchListView
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('profile', views.ProfileView),
router.register('project', views.ProjectView),


urlpatterns = [
    path('', ProjectListView.as_view(), name='homepage'),
    path('user/<str:username>/', UserProjectListView.as_view(), name='user-projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('search/',  SearchListView.as_view(), name='search-users'),
    path('api/', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
