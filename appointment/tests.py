from django.test import TestCase
from django.urls import reverse

class AppointmentURLsTest(TestCase):
    def test_appointment_home_url_is_correct(self):
        appointment_home = reverse('appointment:home')
        self.assertEqual(appointment_home, '/appointment/')