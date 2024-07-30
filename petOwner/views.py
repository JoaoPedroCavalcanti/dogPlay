from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from petOwner.forms import RegisterForm

# Create your views here.
def registerPetOwner(req):

    
    form = RegisterForm()
    return render(req, 'petOwner/pages/register.html', context={
        'form': form,
    })
    
def createPetowner(req):
    if not req.POST:
        raise Http404()
    
    POST = req.POST
    req.session['register_form_data'] = POST
    form = RegisterForm(POST)
    
    if form.is_valid():
        form.save()
        messages.success(req, 'Your user is created, please log in.')
        del(req.session['register_form_data'])
        
    return redirect('petOwner:register')
    



