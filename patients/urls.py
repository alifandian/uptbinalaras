from django.urls import path

from . import views

app_name = "patients"
urlpatterns = [
    path("", views.list_patient, name="list_patient"),
    path("addpatient/", views.add_patient, name="add_patient"),
    path("addpatient/add", views.add, name="add"),
    path("<int:patient_id>/", views.detail_patient, name="detail_patient"),
]