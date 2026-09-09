from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Patient
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Menampilkan halaman pasien

#def list_patient(request):
    #all_patients = Patient.objects.all()
    #context = {"patients" : all_patients}
    #return render(request, "patients/list_patient.html", context)

class ListPatient(LoginRequiredMixin, generic.ListView):
    context_object_name = "patients"
    template_name = "patients/list_patient.html"

    def get_queryset(self):
        return Patient.objects.all()

    def get_context_data(self, **kwargs):
        # WAJIB panggil super() dulu, supaya context bawaan (mis. "patients")
        # tetap ada, baru kita tambahkan context custom di bawahnya.
        context = super().get_context_data(**kwargs)

        context["active_count"] = Patient.objects.filter(status='active').count()
        context["sakit_count"] = Patient.objects.filter(status='sakit').count()
        context["dikembalikan_count"] = Patient.objects.filter(status='dikembalikan').count()
        context["hilang_count"] = Patient.objects.filter(status='hilang').count()
        context["meninggal_count"] = Patient.objects.filter(status='meninggal').count()

        return context
#form penambahan pasien
@login_required
def add_patient(request):
    return render(request, "patients/add_patient.html", )

#detail setiap pasien
#def detail_patient(request, patient_id):
    patientID = get_object_or_404(Patient, pk=patient_id)
    context = {"patient" : patientID}
    return render(request, "patients/detail_patient.html", context)

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Patient
    template_name = "patients/detail_patient.html"

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

def delete(request,pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return HttpResponseRedirect(reverse("patients:list_patient"))

def edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "POST":
        try:
            patient.full_name = request.POST["full_name"]
            patient.gender = request.POST["gender"]
            patient.birth_date = request.POST["birth_date"]
            patient.admission_date = request.POST["admission_date"]
            patient.status = request.POST["status"]
            patient.address = request.POST["address"]
        except KeyError:
            return render(request, "patients/edit_patient.html", {
                "patient": patient,
                "error_message": "Anda tidak mengisi form dengan lengkap.",
            })
        else:
            patient.save()
            return HttpResponseRedirect(reverse("patients:list_patient"))

    # request.method == "GET" -> tampilkan form terisi data pasien saat ini
    return render(request, "patients/edit_patient.html", {"patient": patient})

