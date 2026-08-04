from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Patient

# Create your views here.
# Menampilkan halaman pasien
def list_patient(request):
    all_patients = Patient.objects.all()
    context = {"patients" : all_patients}
    return render(request, "patients/list_patient.html", context)

#form penambahan pasien
def add_patient(request):
    return render(request, "patients/add_patient.html", )

#detail setiap pasien
def detail_patient(request, patient_id):
    patientID = get_object_or_404(Patient, pk=patient_id)
    context = {"patient" : patientID}
    return render(request, "patients/detail_patient.html", context)

def add(request):
    try:
        full_name=request.POST["full_name"]
        gender=request.POST["gender"]
        birth_date=request.POST["birth_date"]
        admission_date=request.POST["admission_date"]
        status=request.POST["status"]
        address=request.POST["address"]

    except KeyError:
        return render(request, 
                      "patients/add_patient.html",
                      {"error_message" : "anda tidak mengisi form dengan lengkap "},)
    
    else :
        p = Patient(full_name=full_name, 
                    gender=gender, 
                    birth_date=birth_date, 
                    admission_date=admission_date,
                    status=status,
                    address=address,)
        p.save()
        return HttpResponseRedirect(reverse("patients:list_patient"))



