
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from mainApp import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    url(r'^logout/$', auth_views.LogoutView, name='logout'),
    url(r'^login/$', auth_views.LoginView, name='login'),
    url(r'^signup/$', core_views.signup, name='signup'),

]
