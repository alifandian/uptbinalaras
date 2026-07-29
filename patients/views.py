from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient

# Create your views here.
# Menampilkan halaman pasien
def list_patient(request):
    all_patients = Patient.objects.all()
    context = {"patients" : all_patients}
    return render(request, "patients/list_patient.html", context)

#form penambahan pasien
def add_patient(request, patient_id):
    return render(request, "patients/add_patient.html", )

#detail setiap pasien
def detail_patient(response):
    return HttpResponse("detail patient")



