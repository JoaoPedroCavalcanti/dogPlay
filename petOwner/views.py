from django.shortcuts import render
from petOwner.forms import RegisterForm

# Create your views here.
def registerPetOwner(req):
    
    form = RegisterForm()
    return render(req, 'petOwner/pages/register.html', context={
        'form': form,
    })