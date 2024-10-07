from django.test import TestCase
from django.urls import reverse

class AppointmentURLsTest(TestCase):
    def test_appointment_home_url_is_correct(self):
        url = reverse('appointment:home')
        self.assertEqual(url, '/appointment/')
        
    def test_appointment_confirmation_url_is_correct(self):
        url = reverse('appointment:confirmation', kwargs= {'id' : 1} )
        self.assertEqual(url, '/appointment/1/')
        
    def test_appointment_myAppointments_url_is_correct(self):
        url = reverse('appointment:myAppointments')
        self.assertEqual(url, '/appointment/my-appointments/')