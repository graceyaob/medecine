from django.contrib import admin

from patient.models import Patient

admin.site.register(Patient)
class BandAdmin(admin.ModelAdmin):
    list_display=("nom","prenom","email","date_de_naissance")
