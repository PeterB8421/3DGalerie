from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:model_id>/detail/', views.detail, name='detail'),
    path('<int:model_id>/edit/', views.edit, name='edit'),
    path('<int:model_id>/delete/', views.delete, name='delete'),
]