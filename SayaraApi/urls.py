from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = (
    # urls for Django Rest Framework SayaraApi
    path('', include(router.urls)),
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
    path('version/detail/<slug:pk>/', views.VersionDetailView.as_view(), name='SayaraApi_version_detail'),
    path('version/delete/<slug:pk>/', views.VersionDeleteView.as_view(), name='SayaraApi_version_delete'),
    path('version/update/<slug:pk>/', views.VersionUpdateView.as_view(), name='SayaraApi_version_update'),
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

urlpatterns += (
    # urls for Fabriquant
    path('fabricant/', views.FabricantListView.as_view(), name='SayaraApi_fabricant_list'),
    path('fabricant/create/', views.FabricantCreateView.as_view(), name='SayaraApi_fabricant_create'),
    path('fabricant/detail/<slug:pk>/', views.FabricantDetailView.as_view(), name='SayaraApi_fabricant_detail'),
    path('fabricant/update/<slug:pk>/', views.FabricantUpdateView.as_view(), name='SayaraApi_fabricant_update'),
    path('fabricant/delete/<slug:pk>/', views.FabricantDeleteView.as_view(), name='SayaraApi_fabricant_delete'),
)

#
urlpatterns += (
    # urls for Couleur
    path('couleur/', views.CouleurListView.as_view(), name='SayaraApi_couleur_list'),
    path('couleur/create/', views.CouleurCreateView.as_view(), name='SayaraApi_couleur_create'),
    path('couleur/detail/<slug:pk>/', views.CouleurDetailView.as_view(), name='SayaraApi_couleur_detail'),
    path('couleur/update/<slug:pk>/', views.CouleurUpdateView.as_view(), name='SayaraApi_couleur_update'),
    path('couleur/delete/<slug:pk>/', views.CouleurDeleteView.as_view(), name='SayaraApi_couleur_delete'),
)

urlpatterns += (
    # urls for Option
    path('option/', views.OptionListView.as_view(), name='SayaraApi_option_list'),
    path('option/create/', views.OptionCreateView.as_view(), name='SayaraApi_option_create'),
    path('option/detail/<slug:pk>/', views.OptionDetailView.as_view(), name='SayaraApi_option_detail'),
    path('option/update/<slug:pk>/', views.OptionUpdateView.as_view(), name='SayaraApi_option_update'),
    path('option/delete/<slug:pk>/', views.OptionDeleteView.as_view(), name='SayaraApi_option_delete'),
)


urlpatterns += (
    # TODO type as a parameter and annonce goes to same view
    path('annonce', views.AnnonceListView.as_view(), name='AnnonceUser'),
    path('annonce/occasion', views.AnnnonceOccasionListView.as_view(), name='Annonce'),
    path('annonce/neuf', views.AnnonceNeufListView.as_view(), name='Annonce'),
)



urlpatterns += (
    # urls for LigneTarif
    path('lignetarif/', views.LigneTarifListView.as_view(), name='SayaraApi_lignetarif_list'),
    path('lignetarif/create/', views.LigneTarifCreateView.as_view(), name='SayaraApi_lignetarif_create'),
    path('lignetarif/detail/<slug:pk>/', views.LigneTarifDetailView.as_view(), name='SayaraApi_lignetarif_detail'),
    path('lignetarif/update/<slug:pk>/', views.LigneTarifUpdateView.as_view(), name='SayaraApi_lignetarif_update'),
)

urlpatterns += (
    # urls for FicheTechnique
    path('fichetechnique/', views.FicheTechniqueListView.as_view(), name='app_name_fichetechnique_list'),
    path('fichetechnique/create/', views.FicheTechniqueCreateView.as_view(), name='app_name_fichetechnique_create'),
    path('fichetechnique/detail/<slug:pk>/', views.FicheTechniqueDetailView.as_view(), name='app_name_fichetechnique_detail'),
    path('fichetechnique/update/<slug:pk>/', views.FicheTechniqueUpdateView.as_view(), name='app_name_fichetechnique_update'),
)