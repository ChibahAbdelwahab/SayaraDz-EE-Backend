from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, views
from rest_framework.response import Response

from .models import *
from .serializers import *


class MarqueListView(generics.ListAPIView):
    model = Marque
    serializer_class = MarqueSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Marque.objects.all()
        query_nom = self.request.GET.get("nomMarque", "")
        query_idModele = self.request.GET.get("pk", "")
        if query_nom is not "":
            queryset = queryset.filter(Q(nomMarque=query_nom))
        if query_idModele is not "":
            queryset = queryset.filter(Q(pk=query_idModele))

        return queryset


class MarqueCreateView(generics.CreateAPIView):
    queryset = Marque.objects.all()
    serializer_class = MarqueSerializer


class MarqueDetailView(generics.RetrieveAPIView):
    queryset = Marque.objects.all()
    serializer_class = MarqueSerializer


class MarqueUpdateView(generics.UpdateAPIView):
    queryset = Marque.objects.all()
    serializer_class = MarqueSerializer


class MarqueDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Marque, pk=pk)

    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message': 'supprimé'}, status=204)


class VersionListView(generics.ListAPIView):
    model = Version
    serializer_class = VersionSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        # try:
        #     queryset = Version.objects.filter(fabricantVersion_id=self.request.user.profile.Fabricant_id)
        # # except User.profile.RelatedObjectDoesNotExist:
        # except:
        #     return ""

        query_id = self.request.GET.get("pk", "")
        query_modele_id = self.request.GET.get("modeleId", "")
        query_modele_name = self.request.GET.get("modele", "")
        query_marque_name = self.request.GET.get("marque", "")

        if query_id is not "":
            return Version.objects.filter(Q(pk=query_id))
        if query_modele_id is not "":
            return Version.objects.filter(Q(modeleVersion_id=query_modele_id))
        if query_modele_name is not "":
            return Version.objects.filter(Q(modeleVersion__nomModele=query_modele_name))
        if query_marque_name is not "":
            print(query_marque_name)
            return Version.objects.filter(
                Q(modeleVersion__nomModele__marqueModele__nomMarque__icontains=query_marque_name))

        return Version.objects.all()


class VersionCreateView(generics.CreateAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionCreateSerializer


class VersionDetailView(generics.RetrieveAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


class VersionUpdateView(generics.UpdateAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionCreateSerializer


class VersionDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Version, pk=pk)

    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message': 'supprimé'}, status=204)


class ModeleListView(generics.ListAPIView):
    model = Modele
    serializer_class = ModeleSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Modele.objects.all()

        query_marque_id = self.request.GET.get("marqueId", "")

        if query_marque_id is not "":
            queryset = queryset.filter(Q(nomModele__marqueModele_id=query_marque_id))
        return queryset


class ListModeleView(generics.ListAPIView):
    queryset = Modele.objects.all()
    serializer_class = ModeleSerializer


class ModeleCreateView(generics.CreateAPIView):
    queryset = Modele.objects.all()
    serializer_class = ModeleCreateSerializer


class ModeleDetailView(generics.RetrieveAPIView):
    queryset = Modele.objects.all()
    serializer_class = ModeleSerializer


class ModeleUpdateView(generics.UpdateAPIView):
    queryset = Modele.objects.all()
    serializer_class = ModeleUpdateSerializer


class ModeleDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Modele, pk=pk)

    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message': 'supprimé'}, status=204)


class FabricantListView(generics.ListAPIView):
    model = Fabricant
    serializer_class = FabricantSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Fabricant.objects.all()
        query_nom = self.request.GET.get("nomFabricant", "")
        query_id = self.request.GET.get("pk", "")
        if query_nom is not "":
            queryset = queryset.filter(Q(nomFabricant=query_nom))
        if query_id is not "":
            queryset = queryset.filter(Q(pk=query_id))

        return queryset


class FabricantCreateView(generics.CreateAPIView):
    queryset = Fabricant.objects.all()
    serializer_class = FabricantSerializer


class FabricantDetailView(generics.RetrieveAPIView):
    queryset = Fabricant.objects.all()
    serializer_class = FabricantSerializer


class FabricantUpdateView(generics.UpdateAPIView):
    queryset = Fabricant.objects.all()
    serializer_class = FabricantSerializer


class FabricantDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Fabricant, pk=pk)

    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message': 'supprimé'}, status=204)


class AnnnonceOccasionListView(generics.ListAPIView):
    models = Annonce
    serializer_class = AnnonceOccasionSerializer

    def get_queryset(self, *args, **kwargs):
        # TODO add more filters
        queryset = Annonce.objects.all().select_related('idVehicule')
        query_d1 = self.request.GET.get("date1", "")
        query_d2 = self.request.GET.get("date2", "")
        query_km1 = self.request.GET.get("km1", "")
        query_km2 = self.request.GET.get("km2", "")
        query_prix1 = self.request.GET.get("prix1", "")
        query_prix2 = self.request.GET.get("prix2", "")
        query_marque = self.request.GET.get("marque", "")

        if query_d1 is not "":
            queryset = queryset.filter(Q(idVehicule__date__gte=query_d1))

        if query_d2 is not "":
            queryset = queryset.filter(Q(idVehicule__date__lte=query_d2))

        if query_km1 is not "":
            queryset = queryset.filter(Q(idVehicule__kilometrage__gte=query_km1))

        if query_km2 is not "":
            queryset = queryset.filter(Q(idVehicule__kilometrage__lte=query_km2))

        if query_prix1 is not "":
            queryset = queryset.filter(Q(prix__gte=query_prix1))

        if query_prix2 is not "":
            queryset = queryset.filter(Q(prix__lte=query_prix2))

        if query_marque is not "":
            queryset = queryset.filter(Q(idVehicule__model__marqueModele__nomMarque__icontains=query_marque))

        return queryset


class AnnonceListView(generics.ListAPIView):
    models = Annonce
    serializer_class = AnnonceOccasionSerializer

    def get_queryset(self, *args, **kwargs):
        query_user = self.request.user.id or None
        if query_user is not None:
            return Annonce.objects.filter(Q(idUser=query_user))

        return Annonce.objects.all()


class AnnonceNeufListView(generics.ListAPIView):
    models = VehiculeNeuf
    serializer_class = AnnnonceNeufSerializer

    def get_queryset(self, *args, **kwargs):

        queryset = VehiculeNeuf.objects.all()

        query_nom = self.request.GET.get("numChassis", "")
        query_prix = self.request.GET.get("prix", "")
        query_idModele = self.request.GET.get("idVehicle", "")

        if query_nom is not "":
            queryset = queryset.filter(Q(idMarque=query_nom))
        if query_idModele is not "":
            queryset = queryset.filter(Q(nomMarque=query_idModele))
        if query_prix is not "":
            queryset = queryset.filter(Q(prix=query_prix))

        return queryset


class CouleurListView(generics.ListAPIView):
    model = Couleur
    serializer_class = CouleurSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Couleur.objects.all()
        query_id = self.request.GET.get("pk", "")
        query_nom = self.request.GET.get("nomCouleur", "")
        query_code = self.request.GET.get("codeCouleur", "")
        query_modele = self.request.GET.get("modeleCouleur", "")

        if query_id is not "":
            queryset = queryset.filter(Q(pk=query_nom))
        if query_nom is not "":
            queryset = queryset.filter(Q(NomCouleur=query_nom))
        if query_code is not "":
            queryset = queryset.filter(Q(CodeCouleur=query_id))
        if query_modele is not "":
            queryset = queryset.filter(Q(ModeleCouleur=query_modele))
        return queryset


class CouleurCreateView(generics.CreateAPIView):
    queryset = Couleur.objects.all()
    serializer_class = CouleurSerializer


class CouleurDetailView(generics.RetrieveAPIView):
    queryset = Couleur.objects.all()
    serializer_class = CouleurSerializer


class CouleurUpdateView(generics.UpdateAPIView):
    queryset = Couleur.objects.all()
    serializer_class = CouleurSerializer


class CouleurDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Couleur, pk=pk)

    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message': 'supprimé'}, status=204)


class OptionListView(generics.ListAPIView):
    model = Option
    serializer_class = OptionSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Option.objects.all()
        query_nom = self.request.GET.get("nomOption", "")
        query_id = self.request.GET.get("codeOption", "")
        if query_nom is not "":
            queryset = queryset.filter(Q(nomOption=query_nom))
        if query_id is not "":
            queryset = queryset.filter(Q(idOption=query_id))
        return queryset


class OptionDetailView(generics.RetrieveAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class OptionUpdateView(generics.UpdateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class OptionCreateView(generics.CreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    # def perform_create(self, serializer):
    #     #     if "FabricantOption_id" not in serializer._kwargs["data"]:
    #     #         serializer.save(fabricantOption_id=Fabricant.objects.get(pk=1))
    #     #     else: serializer.save()


class OptionDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Option, pk=pk)

    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message': 'supprimé'}, status=204)


class LigneTarifListView(generics.ListAPIView):
    model = LigneTarif
    serializer_class = LigneTarifSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = LigneTarif.objects.all()
        return queryset


class LigneTarifDetailView(generics.RetrieveAPIView):
    model = LigneTarif
    serializer_class = LigneTarifSerializer


class LigneTarifUpdateView(generics.UpdateAPIView):
    model = LigneTarif
    serializer_class = LigneTarifSerializer


class LigneTarifCreateView(generics.CreateAPIView):
    model = LigneTarif
    serializer_class = LigneTarifSerializer


class LigneTarifDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(LigneTarif, pk=pk)

    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message': 'supprimé'}, status=204)


# Fiche Technique
class FicheTechniqueListView(generics.ListAPIView):
    model = FicheTechnique
    serializer_class = FicheTechniqueViewAllSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = FicheTechnique.objects.all()
        return queryset


class FicheTechniqueDetailView(generics.RetrieveAPIView):
    model = FicheTechnique
    serializer_class = FicheTechniqueSerializer


class FicheTechniqueUpdateView(generics.UpdateAPIView):
    model = FicheTechnique
    serializer_class = FicheTechniqueSerializer


class FicheTechniqueCreateView(generics.CreateAPIView):
    model = FicheTechnique
    serializer_class = FicheTechniqueSerializer


class FicheTechniqueDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(FicheTechnique, pk=pk)

    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message': 'supprimé'}, status=204)
