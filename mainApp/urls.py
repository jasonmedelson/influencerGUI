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
    path('tag/add/', views.TagCreate.as_view(), name='tag-add'),
    path('tag/add/csv', views.TagCreateCSV, name='tag-add-csv'),
    path('tag/<int:pk>/', views.TagUpdate.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', views.TagDelete.as_view(), name='tag-delete'),
    path('event/add/', views.EventCreate.as_view(), name='event-add'),
    path('event/<int:pk>/', views.EventUpdate.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),

]
