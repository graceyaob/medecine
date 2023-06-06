from django.shortcuts import render,redirect
from patient.models import Patient
from patient.forms import PatientForm
from django.contrib.auth.models import User



 
def liste(request):
    patients = Patient.objects.all()
    return render(request, 'patient/liste.html',{'patients': patients})


"""def patient_detail(request, id):  # notez le paramètre id supplémentaire
   patient = Patient.objects.get(id=id)  
   return render(request, 'patient/patient_detail.html',{'patient': patient}) # nous passons l'id au modèle"""


def patient_delete(request, id):
    patient = Patient.objects.get(id=id)

    if request.method == 'POST':
        # supprimer le patient de la base de données
        patient.delete()
        # rediriger vers la liste 
        return redirect('liste')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,'patient/patient_delete.html',{'patient': patient})


def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            # créer un nouveau patient et le sauvegarder dans la db
            form.save()
            return redirect('liste')

    else:
        form = PatientForm()

    return render(request,'patient/patient_create.html', {'form': form})
    

def patient_modify(request, id):
    patient = Patient.objects.get(id = id)

    if request.method == 'POST':
        # form est rendu avec les paramètres du patient et la methode est post
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('liste')
    else:
        form = PatientForm(instance=patient)

    return render(request,'patient/patient_modify.html',{'form': form, "patient":patient})

