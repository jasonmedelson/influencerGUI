from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #/influencer/add
    # url(r'^influencer/add/$', views.InfluencerCreate.as_view(), name='influencer-add'),
    path('influencer/add/', views.InfluencerCreate.as_view(), name='influencer-add'),
    path('influencer/<uuid:pk>/', views.InfluencerUpdate.as_view(), name='influencer-update'),
    path('influencer/<uuid:pk>/delete/', views.InfluencerDelete.as_view(), name='influencer-delete'),
]
