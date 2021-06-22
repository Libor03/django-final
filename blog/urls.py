from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django_diy_blog import settings
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('animals/', views.AnimalListView.as_view(), name='animal-list'),
    path('animals/<int:pk>/', views.AnimalDetailView.as_view(), name='animal-detail'),
    path('animals/create/', views.AnimalCreate.as_view(), name='animal-create'),
    path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animal-update'),
    path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animal-delete'),
]
