from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('maps/',views.maps, name = 'maps'),
    path('maps/3dmap',views.mapsd, name = 'mapsd'),
    path('login/', views.login , name = 'login'),
    path('sponsors/', views.sponsors , name = 'sponsors'),
    path('team/', views.team , name = 'team'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('social/', views.social, name = 'social'),
    path('events/', views.events , name = 'events'),
    
]