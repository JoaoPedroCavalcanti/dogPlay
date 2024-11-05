from django.urls import reverse
from rest_framework import test

class AppointmentAPIv2Test(test.APITestCase):
    def test_appointment_api_list_returns_status_code_200(self):
        api_url = reverse('appointment:appointment-api-list')
        response = self.client.get(api_url)
        self.assertEqual(response.status_code, 200)