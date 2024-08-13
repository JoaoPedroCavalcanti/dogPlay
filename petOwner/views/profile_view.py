from django.views.generic import TemplateView
from petOwner.models import Profile
from django.shortcuts import get_object_or_404


class ProfileView(TemplateView):
    template_name = 'petOwner/pages/profile.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        profile_id = context.get("id")
        profile = get_object_or_404(Profile, id=profile_id)
        
        return self.render_to_response({
            'profile':profile
        })