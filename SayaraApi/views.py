from attr import exceptions
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, views
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .models import *
from .serializers import *


# Marque views ###########################################################################


class MarqueListView(generics.ListAPIView):
    model = Marque
    serializer_class = MarqueSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Marque.objects.all()
        query_nom = self.request.GET.get("nomMarque", None)
        query_idModele = self.request.GET.get("pk", None)
        if query_nom is not None:
            queryset = queryset.filter(Q(nomMarque=query_nom))
        if query_idModele is not None:
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


# Version views ###########################################################################


class VersionListView(generics.ListAPIView):
    model = Version
    serializer_class = VersionSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        # try:
        #     queryset = Version.objects.filter(fabricantVersion_id=self.request.user.profile.Fabricant_id)
        # # except User.profile.RelatedObjectDoesNotExist:
        # except:
        #     return None

        query_id = self.request.GET.get("pk", None)
        if query_id is not None:
            return Version.objects.filter(pk=query_id)

        query_modele_id = self.request.GET.get("modeleId", None)
        if query_modele_id is not None:
            return Version.objects.filter(modeleVersion_id=query_modele_id)

        return Version.objects.all()


class VersionCreateView(generics.CreateAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


class VersionDetailView(generics.RetrieveAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


class VersionUpdateView(generics.UpdateAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


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

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Modele.objects.all()

        query_marque_id = self.request.GET.get("marqueId", None)

        if query_marque_id is not None:
            queryset = queryset.filter(Q(nomModele__marqueModele_id=query_marque_id))
        return queryset


class ListModeleView(generics.ListAPIView):
    queryset = Modele.objects.all()
    serializer_class = ModeleSerializer


class ModeleCreateView(generics.CreateAPIView):
    queryset = Modele.objects.all()
    serializer_class = ModeleSerializer


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
        query_nom = self.request.GET.get("nomFabricant", None)
        query_id = self.request.GET.get("pk", None)
        if query_nom is not None:
            queryset = queryset.filter(Q(nomFabricant=query_nom))
        if query_id is not None:
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
        return get_object_or_404(Marque, pk=pk)

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
        query_d1 = self.request.GET.get("date1", None)
        query_d2 = self.request.GET.get("date2", None)
        query_km1 = self.request.GET.get("km1", None)
        query_km2 = self.request.GET.get("km2", None)
        query_marque = self.request.GET.get("Marque", None)

        if query_d1 is not None:
            queryset = queryset.filter(Q(idVehicule__date__gte=query_d1))

        if query_d2 is not None:
            queryset = queryset.filter(Q(idVehicule__date__lte=query_d2))

        if query_km1 is not None:
            queryset = queryset.filter(Q(idVehicule__kilometrage__gte=query_km1))

        if query_km2 is not None:
            queryset = queryset.filter(Q(idVehicule__kilometrage__lte=query_km2))

        if query_marque is not None:
            queryset = queryset.filter(Q(nomMarque=query_marque))

        return queryset

class AnnnonceNeufListView(generics.ListAPIView):
    models = VehiculeNeuf
    serializer_class = VehiculeNeufSerializer

    def get_queryset(self, *args, **kwargs):

        queryset = VehiculeNeuf.objects.all()

        query_nom = self.request.GET.get("numChassis", None)
        query_prix = self.request.GET.get("prix", None)
        query_idModele = self.request.GET.get("idVehicle", None)

        if query_nom is not None:
            queryset = queryset.filter(Q(idMarque=query_nom))
        if query_idModele is not None:
            queryset = queryset.filter(Q(nomMarque=query_idModele))
        if query_prix is not None:
            queryset = queryset.filter(Q(prix=query_prix))

        return queryset


class CouleurListView(generics.ListAPIView):
    model = Couleur
    serializer_class = CouleurSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Couleur.objects.all()
        query_id = self.request.GET.get("pk", None)
        query_nom = self.request.GET.get("nomCouleur", None)
        query_code = self.request.GET.get("codeCouleur", None)
        query_modele = self.request.GET.get("modeleCouleur", None)

        if query_id is not None:
            queryset = queryset.filter(Q(pk=query_nom))
        if query_nom is not None:
            queryset = queryset.filter(Q(NomCouleur=query_nom))
        if query_code is not None:
            queryset = queryset.filter(Q(CodeCouleur=query_id))
        if query_modele is not None:
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
        return get_object_or_404(Marque, pk=pk)

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
        query_nom = self.request.GET.get("nomOption", None)
        query_id = self.request.GET.get("codeOption", None)
        if query_nom is not None:
            queryset = queryset.filter(Q(nomOption=query_nom))
        if query_id is not None:
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
        return get_object_or_404(Marque, pk=pk)

    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message': 'supprimé'}, status=204)

