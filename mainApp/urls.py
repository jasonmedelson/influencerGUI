from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #/influencer/add
    # url(r'^influencer/add/$', views.InfluencerCreate.as_view(), name='influencer-add'),
    path('influencer/add/', views.InfluencerCreate, name='influencer-add'),
    path('influencer/<uuid:pk>/', views.InfluencerUpdate, name='influencer-update'),
    path('influencer/<uuid:pk>/delete/', views.InfluencerDelete.as_view(), name='influencer-delete'),
    path('influencer/add/csv', views.InfluencerCreateCSV, name='influencer-add-csv'),
    path('tag/add/', views.TagCreate.as_view(), name='tag-add'),
    path('tag/add/csv', views.TagCreateCSV, name='tag-add-csv'),
    path('tag/<int:pk>/', views.TagUpdate, name='tag-update'),
    path('tag/<int:pk>/delete/', views.TagDelete.as_view(), name='tag-delete'),
    path('event/add/', views.EventCreate.as_view(), name='event-add'),
    path('event/add/csv', views.EventCreateCSV, name='event-add-csv'),
    path('event/<int:pk>/', views.EventUpdate, name='event-update'),
    path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),
    path('list/', views.lists, name='lists-home'),
    path('list/add', views.ListCreate, name='lists-add'),
    path('list/<uuid:pk>/', views.ListUpdate, name='list-update'),
    path('list/<uuid:pk>/delete/', views.ListDelete.as_view(), name='list-delete'),
    path('test/', views.Test, name='test-url')

]
