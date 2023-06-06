from django import forms
from patient.models import Patient

class PatientUsForm(forms.Form):
   nom = forms.CharField(required=False)
   prenom = forms.CharField(required=False)
   date_de_naissance = forms.DateField()
   email = forms.EmailField()
   

class PatientForm(forms.ModelForm):
   class Meta:
        model = Patient
        fields = '__all__'