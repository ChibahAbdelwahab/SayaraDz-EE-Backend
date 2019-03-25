from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

admin.site.register(VehiculeOccasion)
admin.site.register(VehiculeNeuf)
admin.site.register(Marque)
admin.site.register(Version)
admin.site.register(Modele)
admin.site.register(Annonce)
admin.site.register(Fabricant)
admin.site.register(Couleur)
admin.site.register(Option)
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
