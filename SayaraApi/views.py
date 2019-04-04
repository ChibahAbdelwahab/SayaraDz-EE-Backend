from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import *
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import VehiculeForm, MarqueForm, VersionForm, ModeleForm
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import *




#Marque views ###########################################################################



class MarqueListView(generics.ListAPIView):
    model = Marque
    serializer_class = MarqueSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Marque.objects.all()
        query_nom = self.request.GET.get("idMarque", None)
        query_idModele = self.request.GET.get("nomMarque", None)
        if query_nom is not None:
            queryset = queryset.filter(Q(idMarque=query_nom))
        if query_idModele is not None:
            queryset = queryset.filter(Q(nomMarque=query_idModele))

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



#Version views ###########################################################################



class VersionListView(generics.ListAPIView):
    model = Version
    serializer_class = VersionSerializer

    # pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Version.objects.all()
        query_nom            = self.request.GET.get("nomVersion",None)
        query_idModele   = self.request.GET.get("idVersion",None)
        query_code   = self.request.GET.get("codeVersion",None)
        query_marqueModele          = self.request.GET.get("modeleVersion",None)
        if query_nom is not None:
            queryset = queryset.filter(Q(nomVersion = query_nom))
        if query_code is not None:
            queryset = queryset.filter(Q(codeVersion = query_code))
        if query_idModele is not None:
            queryset = queryset.filter(Q(idVersion = query_idModele))
        if query_marqueModele is not None:
            queryset = queryset.filter(Q(modeleVersion=query_marqueModele))

        return queryset


class VersionCreateView(generics.CreateAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


class VersionDetailView(generics.RetrieveAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


class VersionUpdateView(generics.UpdateAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionUpdateSerializer


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
        query_nom            = self.request.GET.get("nomModele",None)
        query_idModele   = self.request.GET.get("idModele",None)
        query_code   = self.request.GET.get("codeModele",None)
        query_marqueModele          = self.request.GET.get("fabricantModele",None)
        if query_nom is not None:
            queryset = queryset.filter(Q(nomModele=query_nom))
        if query_idModele is not None:
            queryset = queryset.filter(Q(idModele=query_idModele))
        if query_marqueModele is not None:
            queryset = queryset.filter(Q(fabricantModele = query_marqueModele))
        if query_code is not None:
            queryset = queryset.filter(Q(codeVersion = query_code))

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
        query_id = self.request.GET.get("idFabricant", None)
        if query_nom is not None:
            queryset = queryset.filter(Q(nomFabricant=query_nom))
        if query_id is not None:
            queryset = queryset.filter(Q(idFabricant=query_id))

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

        queryset = Annonce.objects.all().select_related('idVehicule')
        query_nom = self.request.GET.get("idAnnonce", None)
        query_idModele = self.request.GET.get("titre", None)
        if query_nom is not None:
            queryset = queryset.filter(Q(idMarque=query_nom))
        if query_idModele is not None:
            queryset = queryset.filter(Q(nomMarque=query_idModele))

        return queryset


class AnnnonceNeufListView(generics.ListAPIView):
    models = VehiculeNeuf
    serializer_class = VehiculeNeufSerializer

    def get_queryset(self, *args, **kwargs):

        queryset = VehiculeNeuf.objects.all()
        query_nom = self.request.GET.get("numChassis", None)
        query_idModele = self.request.GET.get("idVehicle", None)
        if query_nom is not None:
            queryset = queryset.filter(Q(idMarque=query_nom))
        if query_idModele is not None:
            queryset = queryset.filter(Q(nomMarque=query_idModele))

        return queryset

class CouleurListView(generics.ListAPIView):
    model = Couleur
    serializer_class = CouleurSerializer
    def get_queryset(self, *args, **kwargs):
        queryset = Couleur.objects.all()
        query_idMarque = self.request.GET.get("idMarque",None)
        query_nom  = self.request.GET.get("nomCouleur",None)
        query_id   = self.request.GET.get("codeCouleur",None)
        if query_idMarque is not None:
            queryset = queryset.filter(Q(nomCouleur=query_nom))
        if query_nom is not None:
            queryset = queryset.filter(Q(nomCouleur = query_nom))
        if query_id is not None:
            queryset = queryset.filter(Q(idCouleur = query_id))
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
        return Response({'message':'supprimé'}, status=204)
    
class OptionListView(generics.ListAPIView):
    model = Option
    serializer_class = OptionSerializer
    #pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Option.objects.all()
        query_nom  = self.request.GET.get("nomOption",None)
        query_id   = self.request.GET.get("codeOption",None)
        queryset = queryset.filter(Q(nomOption = query_nom))
        if query_nom is not None:
            queryset = queryset.filter(Q(nomOption = query_nom))
        if query_id is not None:
            queryset = queryset.filter(Q(idOption = query_id))
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

class OptionDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Marque, pk=pk)
    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message':'supprimé'}, status=204)