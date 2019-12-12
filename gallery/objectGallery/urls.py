from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('tagCreate/<int:model_id>/<str:tag>/', views.ajaxAddTag, name="ajaxAddTag"),
    path('tagDelete/<int:model_id>/<int:tag_id>/', views.ajaxDeleteTag, name="ajaxDeleteTag"),
    path('<int:model_id>/detail/', views.detail, name='detail'),
    path('<int:model_id>/edit/', views.edit, name='edit'),
    path('<int:model_id>/delete/', views.delete, name='delete'),
    path('<int:model_id>/addGallery/', views.addGallery, name='addGallery'),
    path('<int:model_id>/editGallery/', views.editGallery, name="editGallery"),
    path('<int:model_id>/delete/ajax/', views.ajaxDelete, name="ajaxDelete"),
    path('img/<int:img_id>/delete/ajax/', views.ajaxDeleteFromGallery, name="ajaxDeleteFromGallery"),
    path('img/<int:img_id>/delete/', views.deleteFromGallery, name="deleteFromGallery"),
    path('log/in', views.user_login, name="log_in"),
    path('log/out', views.user_logout, name="log_out"),
    path('delall/do', views.deleteAll, name="delalldo"),
    path('delall', views.delall, name="delall"),
]