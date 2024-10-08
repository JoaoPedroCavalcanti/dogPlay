from django.test import TestCase
from django.urls import reverse, resolve
from appointment import views
        
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
        
    def test_appointment_home_view_function_returns_code_200(self):
        response = self.client.get(reverse('appointment:home'))
        self.assertEqual(response.status_code, 200)
        
    def test_appointment_home_view_function_load_correct_template(self):
        response = self.client.get(reverse('appointment:home'))
        self.assertTemplateUsed(response, 'appointment/pages/appointmentHome.html')