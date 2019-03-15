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
    path('vehicule/', views.VehiculeListView.as_view(), name='SayaraApi_vehicule_list'),
    path('vehicule/create/', views.VehiculeCreateView.as_view(), name='SayaraApi_vehicule_create'),
    path('vehicule/detail/<slug:pk>/', views.VehiculeDetailView.as_view(), name='SayaraApi_vehicule_detail'),
    path('vehicule/update/<slug:pk>/', views.VehiculeUpdateView.as_view(), name='SayaraApi_vehicule_update'),
    path('vehicule/list', views.VehiculeListView.as_view(), name="vehicule_List"),
)

urlpatterns += (
    # urls for Marque
    path('marque/', views.MarqueListView.as_view(), name='SayaraApi_marque_list'),
    path('marque/create/', views.MarqueCreateView.as_view(), name='SayaraApi_marque_create'),
    path('marque/detail/<slug:pk>/', views.MarqueDetailView.as_view(), name='SayaraApi_marque_detail'),
    path('marque/delete/<slug:pk>/', views.MarqueDeleteView.as_view(), name='SayaraApi_marque_delete'),
    path('marque/update/<slug:pk>/', views.MarqueUpdateView.as_view(), name='SayaraApi_marque_update'),
)


urlpatterns += (
    # urls for Version
    path('version/', views.VersionListView.as_view(), name='SayaraApi_version_list'),
    path('version/create/', views.VersionCreateView.as_view(), name='SayaraApi_version_create'),
    path('version/detail/<int:pk>/', views.VersionDetailView.as_view(), name='SayaraApi_version_detail'),
    path('version/update/<int:pk>/', views.VersionUpdateView.as_view(), name='SayaraApi_version_update'),
)


urlpatterns += (
    # urls for Modele
    path('modele/', views.ModeleListView.as_view(), name='SayaraApi_modele_list'),
    path('modele/create/', views.ModeleCreateView.as_view(), name='SayaraApi_modele_create'),
    path('modele/detail/<slug:pk>/', views.ModeleDetailView.as_view(), name='SayaraApi_modele_detail'),
    path('modele/update/<slug:pk>/', views.ModeleUpdateView.as_view(), name='SayaraApi_modele_update'),
    path('modele/delete/<slug:pk>/', views.ModeleDeleteView.as_view(), name='SayaraApi_modele_delete'),
    path('modele/list', views.ListModeleView.as_view(), name="modele_List"),
)
