from django.shortcuts import render

# Create your views here.
def registerPetOwner(req):
    return render(req, 'petOwner/pages/register.html')