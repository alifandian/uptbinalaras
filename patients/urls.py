from django.urls import path

from . import views

app_name = "patients"
urlpatterns = [
    path("", views.ListPatient.as_view(), name="list_patient"),
    path("addpatient/", views.add_patient, name="add_patient"),
    path("addpatient/add", views.add, name="add"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail_patient"),
    path("<int:pk>/delete/", views.delete, name='delete'),
    path("<int:pk>/edit/", views.edit, name='edit')

]