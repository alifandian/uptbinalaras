from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_patient, name="list_patient"),
    path("addpatient/", views.add_patient, name="add_patient"),
    path("detailpatient/", views.detail_patient, name="detail_patient"),
]