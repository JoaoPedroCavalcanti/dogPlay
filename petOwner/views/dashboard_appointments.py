from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from appointment.models import Appointment
from utils.past_and_future_appointments import past_and_future_appointments

    
@method_decorator(
    login_required(login_url='petOwner:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardAppointments(ListView):
    model = Appointment
    context_object_name = 'future_appointments'
    ordering = ['-id']
    template_name = 'petOwner/pages/dashboard.html'
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            petOwner=self.request.user,
        )
        return qs
    
    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        past_appointments, future_appointments = past_and_future_appointments(self.request)
        petOwnerName = self.request.user
        ctx.update(context={
            'future_appointments': future_appointments,
            'past_appointments': past_appointments,
            'petOwnerName': petOwnerName 
        })
        return ctx
