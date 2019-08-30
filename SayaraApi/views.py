from django.db.models import Q, F
from django.shortcuts import get_object_or_404
from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework.fields import empty
from .models import *
from .serializers import *


class MarqueListView(generics.ListAPIView):
    model = Marque
    serializer_class = MarqueSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Marque.objects.all()
        query_nom = self.request.GET.get("nom", "")
        query_idModele = self.request.GET.get("pk", "")
        if query_nom is not "":
            queryset = queryset.filter(Q(nom=query_nom))
        if query_idModele is not "":
            queryset = queryset.filter(Q(pk=query_idModele))

        return queryset


class MarqueCreateView(generics.CreateAPIView):
    model = Marque
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


class OffreListView(generics.ListAPIView):
    model = Offre
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer


class OffreCreateView(generics.CreateAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer


class OffreDetailView(generics.RetrieveAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer


class OffreUpdateView(generics.UpdateAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer


class OffreDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Offre, pk=pk)

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
        #     queryset = Version.objects.filter(FabricantVersion_id=self.request.user.profile.Fabricant_id)
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
            return Version.objects.filter(Q(modele_id=query_modele_id))
        if query_modele_name is not "":
            return Version.objects.filter(Q(modele__nom=query_modele_name))
        if query_marque_name is not "":
            print(query_marque_name)
            return Version.objects.filter(
                Q(modele__nom__marque__nom__icontains=query_marque_name))

        return Version.objects.all()


class VersionCreateView(generics.CreateAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionCreateSerializer


class VersionDetailView(generics.RetrieveAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionDetailSerializer


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

    # TODO return only Fabricant's marques for Fabricant
    def get_queryset(self, *args, **kwargs):
        queryset = Modele.objects.all()
        marqueId = self.request.GET.get("marqueId", "")
        marque_nom = self.request.GET.get("marque_nom", "")

        if marqueId is not "":
            # TODO check this
            queryset = queryset.filter(ref__marque__pk=marqueId)
        if marque_nom is not "":
            # TODO check this
            queryset = queryset.filter(Q(marque_nom=marque_nom))
        return queryset


class ModeleListViewMobile(generics.ListAPIView):
    model = Modele
    serializer_class = ModeleSerializerMobile

    # TODO return only Fabricant's marques for Fabricant
    def get_queryset(self, *args, **kwargs):
        queryset = Modele.objects.all()
        marqueId = self.request.GET.get("marqueId", "")
        marque_nom = self.request.GET.get("marque_nom", "")

        if marqueId is not "":
            # TODO check this
            queryset = queryset.filter(ref__marque__pk=marqueId)
        if marque_nom is not "":
            # TODO check this
            queryset = queryset.filter(Q(marque_nom=marque_nom))
        return queryset


class RefModeleListView(generics.ListAPIView):
    model = RefModele
    serializer_class = RefModeleSerializer

    def get_queryset(self, *args, **kwargs):
        return RefModele.objects.all()


class VehiculeNeufListView(generics.ListAPIView):
    model = VehiculeNeuf
    serializer_class = VehiculeNeufSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = VehiculeNeuf.objects.all()
        modele = self.request.GET.get("modele_pk", "")
        version = self.request.GET.get("version_pk", "")
        couleur = self.request.GET.get("couleur_pk", "")

        if modele is not "":
            queryset = queryset.filter(Q(modele_pk=modele))
        if version is not "":
            queryset = queryset.filter(Q(version_pk=version))
        if couleur is not "":
            pass
            # queryset = queryset.filter(Q(couleur_pk=Couleur))

        return queryset


class ListModeleView(generics.ListAPIView):
    queryset = Modele.objects.all()
    serializer_class = ModeleSerializer


class ModeleCreateView(generics.CreateAPIView):
    model = Modele
    serializer_class = ModeleCreateSerializer


class RefModeleCreateView(generics.CreateAPIView):
    queryset = RefModele.objects.all()
    serializer_class = RefModeleCreateSerializer


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
        query_nom = self.request.GET.get("nom", "")
        query_id = self.request.GET.get("pk", "")
        if query_nom is not "":
            queryset = queryset.filter(Q(nom=query_nom))
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
        queryset = Annonce.objects.all().select_related('vehicule')
        query_d1 = self.request.GET.get("date1", "")
        query_d2 = self.request.GET.get("date2", "")
        query_km1 = self.request.GET.get("km1", "")
        query_km2 = self.request.GET.get("km2", "")
        query_prix1 = self.request.GET.get("prix1", "")
        query_prix2 = self.request.GET.get("prix2", "")
        query_marque = self.request.GET.get("marque", "")

        if query_d1 is not "":
            queryset = queryset.filter(Q(vehicule__date__gte=query_d1))

        if query_d2 is not "":
            queryset = queryset.filter(Q(vehicule__date__lte=query_d2))

        if query_km1 is not "":
            queryset = queryset.filter(Q(vehicule__kilometrage__gte=query_km1))

        if query_km2 is not "":
            queryset = queryset.filter(Q(vehicule__kilometrage__lte=query_km2))

        if query_prix1 is not "":
            queryset = queryset.filter(Q(prix__gte=query_prix1))

        if query_prix2 is not "":
            queryset = queryset.filter(Q(prix__lte=query_prix2))

        if query_marque is not "":
            queryset = queryset.filter(
                Q(vehicule__Modele__marque__nom__icontains=query_marque))

        return queryset


class AnnonceOccasionDetailView(generics.RetrieveAPIView):
    queryset = Annonce.objects.all().select_related('vehicule')
    serializer_class = AnnonceOccasionSerializer


class AnnonceCreateView(generics.CreateAPIView):
    model = Annonce
    serializer_class = AnnonceCreateSerializer


class AnnonceUpdateView(generics.UpdateAPIView):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceUpdateSerializer


class AnnonceListView(generics.ListAPIView):
    models = Annonce
    serializer_class = AnnonceOccasionSerializer

    def get_queryset(self, *args, **kwargs):
        query_user = self.request.user.id or None
        if query_user is not None:
            return Annonce.objects.filter(Q(user=query_user))

        return Annonce.objects.all()


class AnnonceOccasionDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Annonce, pk=pk)

    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message': 'supprimé'}, status=204)


class AnnonceNeufListView(generics.ListAPIView):
    models = VehiculeNeuf
    serializer_class = AnnnonceNeufSerializer

    def get_queryset(self, *args, **kwargs):

        queryset = VehiculeNeuf.objects.all()

        query_nom = self.request.GET.get("num", "")
        query_prix = self.request.GET.get("prix", "")
        query_idModele = self.request.GET.get("idVehicle", "")

        if query_nom is not "":
            queryset = queryset.filter(Q(idMarque=query_nom))
        if query_idModele is not "":
            queryset = queryset.filter(Q(nom=query_idModele))
        if query_prix is not "":
            queryset = queryset.filter(Q(prix=query_prix))

        return queryset


class AnnonceNeufDetailView(generics.RetrieveAPIView):
    queryset = VehiculeNeuf.objects.all()
    serializer_class = AnnnonceNeufSerializer


class CouleurListView(generics.ListAPIView):
    model = Couleur
    serializer_class = CouleurSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Couleur.objects.all()
        query_id = self.request.GET.get("pk", "")
        query_nom = self.request.GET.get("nom", "")
        query_code = self.request.GET.get("code", "")
        query_modele = self.request.GET.get("modele", "")

        if query_id is not "":
            queryset = queryset.filter(Q(pk=query_nom))
        if query_nom is not "":
            queryset = queryset.filter(Q(nom=query_nom))
        if query_code is not "":
            queryset = queryset.filter(Q(code=query_id))
        if query_modele is not "":
            queryset = queryset.filter(Q(modele=query_modele))
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

    # pagination_class = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Option.objects.all()
        query_nom = self.request.GET.get("nom", "")
        query_id = self.request.GET.get("code", "")
        if query_nom is not "":
            queryset = queryset.filter(Q(nom=query_nom))
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
    #     #         serializer.save(FabricantOption_id=Fabricant.objects.get(pk=1))
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


class LigneTarifCreateView(generics.ListCreateAPIView):
    queryset = LigneTarif.objects.all()
    serializer_class = LigneTarifSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = LigneTarifSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        if isinstance(data, list):  # <- is the main logic
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TarifVersionListView(generics.ListAPIView):
    model = TarifVersion
    serializer_class = TarifVersionSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = TarifVersion.objects.all()
        return queryset


class TarifVersionUpdateView(generics.UpdateAPIView):
    model = TarifVersion
    serializer_class = TarifVersionSerializer


class TarifVersionCreateView(generics.ListCreateAPIView):
    queryset = TarifVersion.objects.all()
    serializer_class = TarifVersionSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TarifVersionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        if isinstance(data, list):  # <- is the main logic
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TarifCouleurListView(generics.ListAPIView):
    model = TarifCouleur
    serializer_class = TarifCouleurSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = TarifCouleur.objects.all()
        return queryset


class TarifCouleurUpdateView(generics.UpdateAPIView):
    model = TarifCouleur
    serializer_class = TarifCouleurSerializer


class TarifCouleurCreateView(generics.ListCreateAPIView):
    queryset = TarifCouleur.objects.all()
    serializer_class = TarifCouleurSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TarifCouleurSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        if isinstance(data, list):  # <- is the main logic
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TarifOptionListView(generics.ListAPIView):
    model = TarifOption
    serializer_class = TarifOptionSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = TarifOption.objects.all()
        return queryset


class TarifOptionUpdateView(generics.UpdateAPIView):
    model = TarifOption
    serializer_class = TarifOptionSerializer


class TarifOptionCreateView(generics.ListCreateAPIView):
    queryset = TarifOption.objects.all()
    serializer_class = TarifOptionSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TarifOptionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        if isinstance(data, list):  # <- is the main logic
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    queryset = FicheTechnique.objects.all()
    serializer_class = FicheTechniqueSerializer


class FicheTechniqueUpdateView(generics.UpdateAPIView):
    model = FicheTechnique
    serializer_class = FicheTechniqueCreateSerializer


class FicheTechniqueCreateView(generics.CreateAPIView):
    model = FicheTechnique
    serializer_class = FicheTechniqueCreateSerializer


class FicheTechniqueDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(FicheTechnique, pk=pk)

    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message': 'supprimé'}, status=204)


# Commande
class CommandeListView(generics.ListAPIView):
    model = Commande
    serializer_class = CommandeViewSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Commande.objects.all()
        return queryset


class CommandeDetailView(generics.RetrieveAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeViewSerializer


class CommandeUpdateView(generics.UpdateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer


class CommandeCreateView(generics.CreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer


class CommandeDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Commande, pk=pk)

    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message': 'supprimé'}, status=204)
