from django.test import TestCase
from .models import Patient
from django.urls import reverse
# Create your tests here.

class PatientListPatientViewTests(TestCase) :
    def test_no_patients(self):
        response = self.client.get(reverse('patients:list_patient'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Belum ada data pasien.")
        self.assertQuerySetEqual(response.context["patients"], [])