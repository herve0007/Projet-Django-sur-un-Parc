from django.urls import path
from . import views
urlpatterns = [

    path("", views.animaux_liste, name="Animaux_list"),
    path('Animaux/<int:pk>/', views.animaux_detail, name='animaux_detail'),
    path('Zonecoeur/', views.zone_coeur_liste, name='ZoneCoeur_list'),
    path('Zonecoeur/<int:pk>/', views.zone_coeur_detail, name='Zonecoeur_detail'),
    path('home/', views.home_view, name='home'),
    path('enregistrement/', views.enregistrement_view, name= 'enregistrement'),
    path('ajoutAnimaux/', views.nouveau_animaux, name='nouveau_animaux'),
    path('ajoutZone/', views.zone_nouveau, name='nouveau_zone'),
    path('delete/<int:pk>/', views.delete_animal, name='delete_animal'),
    path('edit/<int:pk>/', views.edit_animal, name='edit_animal'),
    path('delete_zone/<int:pk>/', views.delete_zone, name='delete_zone'),
    path('edit_zone/<int:pk>/', views.edit_zone, name='edit_zone'),

]