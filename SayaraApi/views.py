from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import *
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import VehiculeForm, MarqueForm, VersionForm, ModeleForm
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import *

class VehiculeListView(generics.ListAPIView):
    model = Vehicule
    serializer_class = VehiculeSerializer
    #pagination_class    = VehiculeListPagination

    def get_queryset(self, *args, **kwargs):
        queryset = Vehicule.objects.all()
        query_pk            = self.request.GET.get("disponible",None)
        query_NumChassis   = self.request.GET.get("numchassis",None)
        query_Version          = self.request.GET.get("version",None)
        if query_pk is not None:
            queryset = queryset.filter(Q(disponible = query_pk))
        if query_NumChassis is not None:
            queryset = queryset.filter(Q(numChassis = query_NumChassis))
        if query_Version is not None:
            queryset = queryset.filter(Q(versionVoiture = query_Version))

        return queryset

class VehiculeCreateView(generics.CreateAPIView):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer


class VehiculeDetailView(generics.RetrieveAPIView):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer


class VehiculeUpdateView(generics.UpdateAPIView):
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeUpdateSerializer

class VehiculeDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Vehicule, pk=pk)
    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message':'supprimé'}, status=204)

class MarqueListView(generics.ListAPIView):
    model = Marque
    serializer_class = MarqueSerializer
    #pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Marque.objects.all()
        query_nom            = self.request.GET.get("idMarque",None)
        query_idModele   = self.request.GET.get("nomMarque",None)
        if query_nom is not None:
            queryset = queryset.filter(Q(idMarque = query_nom))
        if query_idModele is not None:
            queryset = queryset.filter(Q(nomMarque = query_idModele))

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
        return Response({'message':'supprimé'}, status=204)


class VersionListView(generics.ListAPIView):
    model = Version
    serializer_class = VersionSerializer
    #pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Version.objects.all()
        query_nom            = self.request.GET.get("nomVersion",None)
        query_idModele   = self.request.GET.get("codeVersion",None)
        query_marqueModele          = self.request.GET.get("modeleVersion",None)
        if query_nom is not None:
            queryset = queryset.filter(Q(nomVersion = query_nom))
        if query_idModele is not None:
            queryset = queryset.filter(Q(codeVersion = query_idModele))
        if query_marqueModele is not None:
            queryset = queryset.filter(Q(modeleVersion = query_marqueModele))

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
        return Response({'message':'supprimé'}, status=204)


class ModeleListView(generics.ListAPIView):
    model = Modele
    serializer_class = ModeleSerializer
    #pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Modele.objects.all()
        query_nom            = self.request.GET.get("nomModele",None)
        query_idModele   = self.request.GET.get("idModele",None)
        query_marqueModele          = self.request.GET.get("marqueModele",None)
        if query_nom is not None:
            queryset = queryset.filter(Q(nomModele = query_nom))
        if query_idModele is not None:
            queryset = queryset.filter(Q(idModele = query_idModele))
        if query_marqueModele is not None:
            queryset = queryset.filter(Q(marqueModele = query_marqueModele))

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
        return Response({'message':'supprimé'}, status=204)

class FabriquantListView(generics.ListAPIView):
    model = Fabriquant
    serializer_class = FabriquantSerializer
    #pagination_class    = VehiculeListPagination
    def get_queryset(self, *args, **kwargs):
        queryset = Modele.objects.all()
        query_nom            = self.request.GET.get("nomFabriquant",None)
        query_id   = self.request.GET.get("idFabriquant",None)
        if query_nom is not None:
            queryset = queryset.filter(Q(nomFabriquant = query_nom))
        if query_id is not None:
            queryset = queryset.filter(Q(idFabriquant = query_id))

        return queryset
    


class FabriquantCreateView(generics.CreateAPIView):
    queryset = Fabriquant.objects.all()
    serializer_class = FabriquantSerializer


class FabriquantDetailView(generics.RetrieveAPIView):
    queryset = Fabriquant.objects.all()
    serializer_class = FabriquantSerializer


class FabriquantUpdateView(generics.UpdateAPIView):
    queryset = Fabriquant.objects.all()
    serializer_class = FabriquantSerializer

class FabricantDeleteView(views.APIView):
    def get_object(self, pk):
        return get_object_or_404(Marque, pk=pk)
    def delete(self, request, pk, *args, **kwargs):
        thing = self.get_object(pk)
        thing.delete()
        return Response({'message':'supprimé'}, status=204)