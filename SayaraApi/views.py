from django.db.models import Q, F
from django.shortcuts import get_object_or_404
from rest_framework import generics, views, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.fields import empty
from rest_framework.viewsets import ModelViewSet

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

    def get_queryset(self, *args, **kwargs):
        query_user = self.request.user.id or None
        if query_user is not None:
            return Offre.objects.filter(Q(user=query_user))

        return Offre.objects.all()


class OffreAnnonceListView(generics.ListAPIView):
    model = Offre
    queryset = Offre.objects.all()
    serializer_class = OffreSerializer

    def get_queryset(self, *args, **kwargs):
        queryAnnonce = self.request.GET.get("annonce", None)
        if queryAnnonce is not None:
            return Offre.objects.filter(Q(annonce=queryAnnonce))
        return Offre.objects.all()


class OffreCreateView(generics.CreateAPIView):
    queryset = Offre.objects.all()
    serializer_class = OffreCreateSerializer


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


class RefCouleurListView(generics.ListAPIView):
    model = RefCouleur
    serializer_class = RefCouleurSerializer

    def get_queryset(self, *args, **kwargs):
        return RefCouleur.objects.all()


class RefVersionListView(generics.ListAPIView):
    model = RefVersion
    serializer_class = RefVersionSerializer

    def get_queryset(self, *args, **kwargs):
        return RefVersion.objects.all()


class VehiculeNeufListView(generics.ListAPIView):
    model = VehiculeNeuf
    serializer_class = VehiculeNeufSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = VehiculeNeuf.objects.all()
        modele = self.request.GET.get("modele_pk", "")
        version = self.request.GET.get("version_pk", "")
        couleur = self.request.GET.get("couleur_pk", "")

        modele = self.request.GET.get("modele", modele)
        version = self.request.GET.get("version", version)
        couleur = self.request.GET.get("couleur", couleur)

        if modele is not "":
            queryset = queryset.filter(Q(version__modele=modele))
        if version is not "":
            queryset = queryset.filter(Q(version=version))
        if couleur is not "":
            queryset = queryset.filter(Q(version__couleur=couleur))
        return queryset


class VehiculeNeufCreateView(generics.ListCreateAPIView):
    queryset = VehiculeNeuf.objects.all()
    serializer_class = VehiculeNeufSerialiser

    def list(self, request):
        queryset = self.get_queryset()
        serializer = VehiculeNeufSerialiser(queryset, many=True)
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


class ListModeleView(generics.ListAPIView):
    queryset = Modele.objects.all()
    serializer_class = ModeleSerializer


class ModeleCreateView(generics.CreateAPIView):
    model = Modele
    serializer_class = ModeleCreateSerializer


class VehiculeOccasionCreateView(generics.CreateAPIView):
    model = VehiculeOccasion
    serializer_class = VehiculeOccasionCreateSerializer


class RefModeleCreateView(generics.CreateAPIView):
    queryset = RefModele.objects.all()
    serializer_class = RefModeleCreateSerializer


class RefCouleurCreateView(generics.CreateAPIView):
    queryset = Couleur.objects.all()
    serializer_class = RefCouleurCreateSerializer


class RefVersionCreateView(generics.CreateAPIView):
    queryset = Version.objects.all()
    serializer_class = RefVersionCreateSerializer


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
        qcouleur = self.request.GET.get("couleur", "")
        qversion = self.request.GET.get("version", "")
        qmodele = self.request.GET.get("modele", "")
        if query_nom is not "":
            queryset = queryset.filter(Q(idMarque=query_nom))
        if query_idModele is not "":
            queryset = queryset.filter(Q(nom=query_idModele))
        if query_prix is not "":
            queryset = queryset.filter(Q(prix=query_prix))
        if qcouleur is not "":
            queryset = queryset.filter(couleur=qcouleur)
        if qversion is not "":
            queryset = queryset.filter(version=qversion)
        if qmodele is not "":
            queryset = queryset.filter(version__modele=qmodele)
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
    serializer_class = CouleurCreateSerializer


class CouleurDetailView(generics.RetrieveAPIView):
    queryset = Couleur.objects.all()
    serializer_class = CouleurSerializer


class CouleurUpdateView(generics.UpdateAPIView):
    queryset = Couleur.objects.all()
    serializer_class = CouleurCreateSerializer


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
        query_modele = self.request.GET.get("modele", "")
        if query_nom is not "":
            queryset = queryset.filter(Q(nom=query_nom))
        if query_id is not "":
            queryset = queryset.filter(Q(idOption=query_id))
        if query_modele is not "":
            queryset = queryset.filter(Q(modele=query_modele))
        return queryset


class OptionDetailView(generics.RetrieveAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class OptionUpdateView(generics.UpdateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionUpdateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(kwargs["pk"])
        print(request.data["nom"])
        new_ref = request.data.get("nom", None)

        serializer = self.get_serializer(instance)
        self.perform_update(serializer)

        return Response(serializer.data)


class OptionCreateView(generics.CreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionCreateSerializer
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
    queryset = Commande.objects.all()
    serializer_class = CommandeViewSerializer


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


class UserFabricant(ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        try:
            fabricant_id = self.request.user.profile.fabricant.id
            queryset = Profile.objects.filter(is_fabricant=True,
                                              fabricant_id=fabricant_id)
        except Exception as e:
            print(e)
            queryset = Profile.objects.none()
        return queryset

    def create(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProfileCreateSerializer(queryset, many=True)
        return Response(serializer.data)


class CommandeView(ModelViewSet):
    serializer_class = CommandeSerializer
    queryset = Commande.objects.all()

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        serializer = CommandeCreateSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.vehicule.reserve = False
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        print(instance)
        if instance.vehicule is not None:
            vehicule = VehiculeNeuf.objects.get(pk=instance.vehicule.id)
            vehicule.reserve = True
            vehicule.save()
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def propositions(self, request, pk=None):
        instance = self.get_object()
        queryset = VehiculeNeuf.objects.all()
        queryset = queryset.filter(version=instance.version)
        queryset = queryset.filter(couleur=instance.couleur)
        queryset = queryset.filter(options__code__in=instance.options)[0]
        serializer = VehiculeNeufSerialiser(data=queryset)
        return Response(serializer.data)


class FicheTechniqueView(ModelViewSet):
    serializer_class = FicheTechniqueSerializer
    queryset = FicheTechnique.objects.all()
