from django.conf import settings
from django.views.static import serve

from cepsearch import views
from django.urls import path, re_path
from cepsearch.views import view_404, view_500

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),    
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),    
    path('', views.home, name='home'),
    path('users/', views.users, name='users'),
    path('users/new', views.usersNew, name='userNew'),
    path('users/new/save/', views.usersNewSave, name='usersNewSave'),
    path('users/<int:id>', views.usersEdit, name='user'),
    path('users/edit/<int:id>', views.user, name='userEdit'),
    path('users/edit/<int:id>/save', views.usersEdit, name='userEditSave'),
]

handler404 = view_404
handler500 = view_500
