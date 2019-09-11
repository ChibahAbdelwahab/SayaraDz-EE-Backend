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
    path('modele/mobile', views.ModeleListViewMobile.as_view(), name='SayaraApi_modele_list'),
    path('modele/create/', views.ModeleCreateView.as_view(), name='SayaraApi_modele_create'),
    path('modele/detail/<slug:pk>/', views.ModeleDetailView.as_view(), name='SayaraApi_modele_detail'),
    path('modele/update/<slug:pk>/', views.ModeleUpdateView.as_view(), name='SayaraApi_modele_update'),
    path('modele/delete/<slug:pk>/', views.ModeleDeleteView.as_view(), name='SayaraApi_modele_delete'),
    path('modele/list', views.ListModeleView.as_view(), name="modele_List"),
)

urlpatterns += (
    # urls for Modele
    path('refmodele/', views.RefModeleListView.as_view(), name='SayaraApi_Refmodele_list'),
    path('refmodele/create/', views.RefModeleCreateView.as_view(), name='SayaraApi_modele_create'),
    # path('refmodele/detail/<slug:pk>/', views.ModeleDetailView.as_view(), name='SayaraApi_modele_detail'),
    # path('refmodele/update/<slug:pk>/', views.ModeleUpdateView.as_view(), name='SayaraApi_modele_update'),
    # path('refmodele/delete/<slug:pk>/', views.ModeleDeleteView.as_view(), name='SayaraApi_modele_delete'),
    # path('refmodele/list', views.ListModeleView.as_view(), name="modele_List"),
)
urlpatterns += (
    # urls for Modele
    path('refcouleur/', views.RefCouleurListView.as_view(), name='SayaraApi_Refcouleur_list'),
    path('refcouleur/create/', views.RefCouleurCreateView.as_view(), name='SayaraApi_couleur_create'),
)
urlpatterns += (
    # urls for Modele
    path('refversion/', views.RefVersionListView.as_view(), name='SayaraApi_Refversion_list'),
    path('refversion/create/', views.RefVersionCreateView.as_view(), name='SayaraApi_version_create'),
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

#
urlpatterns += (
    # TODO annonce create remove user from available fields
    path('annonce/', views.AnnonceListView.as_view(), name='AnnonceUser'),
    path('annonce/create/', views.AnnonceCreateView.as_view(), name='AnnonceCreate'),
    path('annonce/delete/<slug:pk>/', views.AnnonceOccasionDeleteView.as_view(), name='AnnonceDelete'),
    path('annonce/update/<slug:pk>/', views.AnnonceUpdateView.as_view(), name='AnnonceUpdate'),
    path('annonce/occasion/', views.AnnnonceOccasionListView.as_view(), name='Annonce'),
    path('annonce/occasion/detail/<slug:pk>/', views.AnnonceOccasionDetailView.as_view(), name='AnnonceODetail'),
    path('annonce/neuf/', views.AnnonceNeufListView.as_view(), name='Annonce'),
    path('annonce/neuf/detail/<slug:pk>/', views.AnnonceNeufDetailView.as_view(), name='AnnonceNDetail'),
)

urlpatterns += (
    # urls for LigneTarif
    path('lignetarif/', views.LigneTarifListView.as_view(), name='SayaraApi_lignetarif_list'),
    path('lignetarif/create/', views.LigneTarifCreateView.as_view(), name='SayaraApi_lignetarif_create'),
    path('lignetarif/detail/<slug:pk>/', views.LigneTarifDetailView.as_view(), name='SayaraApi_lignetarif_detail'),
    path('lignetarif/update/<slug:pk>/', views.LigneTarifUpdateView.as_view(), name='SayaraApi_lignetarif_update'),
)
urlpatterns += (
    # urls for tarifoption
    path('tarifoption/', views.TarifOptionListView.as_view(), name='SayaraApi_tarifoption_list'),
    path('tarifoption/create/', views.TarifOptionCreateView.as_view(), name='SayaraApi_tarifoption_create'),
    path('tarifoption/update/<slug:pk>/', views.TarifOptionUpdateView.as_view(), name='SayaraApi_tarifoption_update'),
)
urlpatterns += (
    # urls for tarifversion
    path('tarifversion/', views.TarifVersionListView.as_view(), name='SayaraApi_tarifversion_list'),
    path('tarifversion/create/', views.TarifVersionCreateView.as_view(), name='SayaraApi_tarifversion_create'),
    path('tarifversion/update/<slug:pk>/', views.TarifVersionUpdateView.as_view(),
         name='SayaraApi_tarifversion_update'),
)
urlpatterns += (
    # urls for tarifcouleur
    path('tarifcouleur/', views.TarifCouleurListView.as_view(), name='SayaraApi_tarifcouleur_list'),
    path('tarifcouleur/create/', views.TarifCouleurCreateView.as_view(), name='SayaraApi_tarifcouleur_create'),
    path('tarifcouleur/update/<slug:pk>/', views.TarifCouleurUpdateView.as_view(),
         name='SayaraApi_tarifcouleur_update'),
)

urlpatterns += (
    # urls for FicheTechnique
    path('fichetechnique/', views.FicheTechniqueListView.as_view(), name='app_name_fichetechnique_list'),
    path('fichetechnique/create/', views.FicheTechniqueCreateView.as_view(), name='app_name_fichetechnique_create'),
    path('fichetechnique/detail/<slug:pk>/', views.FicheTechniqueDetailView.as_view(),
         name='app_name_fichetechnique_detail'),
    path('fichetechnique/update/<slug:pk>/', views.FicheTechniqueUpdateView.as_view(),
         name='app_name_fichetechnique_update'),
)

urlpatterns += (
    # urls for Commande
    path('commande/', views.CommandeListView.as_view(), name='app_name_commande_list'),
    path('commande/create/', views.CommandeCreateView.as_view(), name='app_name_commande_create'),
    path('commande/detail/<slug:pk>/', views.CommandeDetailView.as_view(),
         name='app_name_commande_detail'),
    path('commande/update/<slug:pk>/', views.CommandeUpdateView.as_view(),
         name='app_name_commande_update'),
    path('commande/delete/<slug:pk>/', views.CommandeDeleteView.as_view(),
         name='app_name_commande_delete')
)
urlpatterns += (
    # urls for Offre
    path('Offre/', views.OffreListView.as_view(), name='SayaraApi_Offre_list'),
    path('Offre/create/', views.OffreCreateView.as_view(), name='SayaraApi_Offre_create'),
    path('Offre/update/<int:pk>/', views.OffreUpdateView.as_view(), name='SayaraApi_Offre_update'),
)

urlpatterns += (
    # urls for Offre
    path('vehiculeneuf/', views.VehiculeNeufListView.as_view(), name='SayaraApi_Vehicule_list'),
    path('vehiculeneuf/create', views.VehiculeNeufCreateView.as_view(), name='SayaraApi_Vehicule_list'),
    path('vehiculeoccasion/create/', views.VehiculeOccasionCreateView.as_view(), name='SayaraApi_Vehicule_list'),
    # path('Offre/create/', views.OffreCreateView.as_view(), name='SayaraApi_Offre_create'),
    # path('Offre/update/<int:pk>/', views.OffreUpdateView.as_view(), name='SayaraApi_Offre_update'),
)
