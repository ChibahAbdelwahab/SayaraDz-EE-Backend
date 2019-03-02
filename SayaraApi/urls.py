from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()


urlpatterns = (
    # urls for Django Rest Framework SayaraApi
    path('', include(router.urls)),
)

urlpatterns += (
    # urls for Vehicule
    path('SayaraApi/vehicule/', views.VehiculeListView.as_view(), name='SayaraApi_vehicule_list'),
    path('SayaraApi/vehicule/create/', views.VehiculeCreateView.as_view(), name='SayaraApi_vehicule_create'),
    path('SayaraApi/vehicule/detail/<slug:pk>/', views.VehiculeDetailView.as_view(), name='SayaraApi_vehicule_detail'),
    path('SayaraApi/vehicule/update/<slug:pk>/', views.VehiculeUpdateView.as_view(), name='SayaraApi_vehicule_update'),
    path('vehicule/list', views.VehiculeListView.as_view(), name="vehicule_List"),
)

urlpatterns += (
    # urls for Marque
    path('SayaraApi/marque/', views.MarqueListView.as_view(), name='SayaraApi_marque_list'),
    path('SayaraApi/marque/create/', views.MarqueCreateView.as_view(), name='SayaraApi_marque_create'),
    path('SayaraApi/marque/detail/<int:pk>/', views.MarqueDetailView.as_view(), name='SayaraApi_marque_detail'),
    path('SayaraApi/marque/update/<int:pk>/', views.MarqueUpdateView.as_view(), name='SayaraApi_marque_update'),
)

urlpatterns += (
    # urls for Version
    path('SayaraApi/version/', views.VersionListView.as_view(), name='SayaraApi_version_list'),
    path('SayaraApi/version/create/', views.VersionCreateView.as_view(), name='SayaraApi_version_create'),
    path('SayaraApi/version/detail/<int:pk>/', views.VersionDetailView.as_view(), name='SayaraApi_version_detail'),
    path('SayaraApi/version/update/<int:pk>/', views.VersionUpdateView.as_view(), name='SayaraApi_version_update'),
)

urlpatterns += (
    # urls for Modele
    path('SayaraApi/modele/', views.ModeleListView.as_view(), name='SayaraApi_modele_list'),
    path('SayaraApi/modele/create/', views.ModeleCreateView.as_view(), name='SayaraApi_modele_create'),
    path('SayaraApi/modele/detail/<int:pk>/', views.ModeleDetailView.as_view(), name='SayaraApi_modele_detail'),
    path('SayaraApi/modele/update/<int:pk>/', views.ModeleUpdateView.as_view(), name='SayaraApi_modele_update'),
    path('modele/list', views.ListModeleView.as_view(), name="modele_List"),
)

