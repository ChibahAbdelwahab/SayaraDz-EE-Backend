from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from pinax.models.admin import LogicalDeleteModelAdmin


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


class VersionResource(resources.ModelResource):
    class Meta:
        model = Version


class VersionAdmin(ImportExportModelAdmin):
    resource_class = VersionResource


class AnnonceResource(resources.ModelResource):
    class Meta:
        model = Annonce


class AnnonceAdmin(ImportExportModelAdmin):
    resource_class = AnnonceResource


class VehiculeNeufResource(resources.ModelResource):
    class Meta:
        model = VehiculeNeuf


class VehiculeNeufAdmin(ImportExportModelAdmin):
    resource_class = VehiculeNeufResource


class VehiculeOccasionResource(resources.ModelResource):
    class Meta:
        model = VehiculeOccasion


class VehiculeOccasionAdmin(ImportExportModelAdmin):
    resource_class = VehiculeOccasionResource


class OptionResource(resources.ModelResource):
    class Meta:
        model = Option


class OptionAdmin(ImportExportModelAdmin):
    resource_class = OptionResource


class CouleurResource(resources.ModelResource):
    class Meta:
        model = Couleur


class CouleurAdmin(ImportExportModelAdmin):
    resource_class = CouleurResource


class FicheTechniqueResource(resources.ModelResource):
    class Meta:
        model = FicheTechnique


class FicheTechniqueAdmin(ImportExportModelAdmin):
    resource_class = FicheTechniqueResource


class FabricantAdmin(LogicalDeleteModelAdmin):
    list_display = ("pk","__str__", "active")
    list_display_filter = ()

    def get_queryset(self, request):
        qs = self.model._default_manager.all_with_deleted()
        ordering = self.ordering or ()
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    class Meta:
        model = Fabricant


admin.site.register(VehiculeOccasion, VehiculeNeufAdmin)
admin.site.register(VehiculeNeuf, VehiculeOccasionAdmin)
admin.site.register(Marque)
admin.site.register(Version, VersionAdmin)
admin.site.register(Modele)
admin.site.register(Profile)
admin.site.register(Commande)
admin.site.register(RefCouleur)
admin.site.register(RefOption)
admin.site.register(RefModele)
admin.site.register(RefVersion)
admin.site.register(Annonce, AnnonceAdmin)
admin.site.register(Fabricant, FabricantAdmin)
admin.site.register(Couleur, CouleurAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Image)
admin.site.register(TarifOption)
admin.site.register(TarifVersion)
admin.site.register(TarifCouleur)
admin.site.register(Offre)
admin.site.register(FicheTechnique, FicheTechniqueAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)