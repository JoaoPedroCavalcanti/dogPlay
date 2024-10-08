from django.test import TestCase
from django.urls import reverse, resolve
from appointment import views

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
        
class AppointmentViewsTest(TestCase):
    def test_appointment_home_view_function_is_correct(self):
        view = resolve(reverse('appointment:home'))
        self.assertIs(view.func, views.appointmentHome)
        
    def test_appointment_confirmation_view_function_is_correct(self):
        view = resolve(reverse('appointment:confirmation', kwargs= {'id' : 1} ))
        self.assertIs(view.func, views.appointmentConfirmation)
        
    def test_appointment_myAppointments_view_function_is_correct(self):
        view = resolve(reverse('appointment:myAppointments'))
        self.assertIs(view.func, views.my_appointments)