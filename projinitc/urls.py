from cepsearch import views
from django.contrib import admin
from django.urls import path
from cepsearch.views import view_404, view_500

urlpatterns = [
    path('', views.home, name='index'),
    path('users/', views.users, name='users'),
    path('users/new/', views.usersNew, name='userNew'),
    path('users/new/save/', views.usersNewSave, name='usersNewSave'),
    path('users/<int:id>/', views.usersEdit, name='user'),
    path('users/edit/<int:id>/', views.user, name='userEdit'),
    path('users/edit/<int:id>/save/', views.usersEdit, name='userEditSave'),
]

handler404 = view_404
handler500 = view_500
