from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from petOwner.forms import RegisterForm, LoginForm
from django.urls import reverse
from django.contrib.auth import authenticate, login

# Register
def registerPetOwner(req):  
    register_form_data = req.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(req, 'petOwner/pages/register.html', {
        'form': form,
        'form_action': reverse('petOwner:create_register'),
    })
    
def createPetowner(req):
    if not req.POST:
        raise Http404()
    
    POST = req.POST
    req.session['register_form_data'] = POST
    form = RegisterForm(POST)
    
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        
        messages.success(req, 'Your user is created, please log in.')
        del(req.session['register_form_data'])
        return redirect(reverse('petOwner:login'))
        
    return redirect('petOwner:register')


# Login
def loginPetOwner(req):
    form = LoginForm()
    return render(req, 'petOwner/pages/login.html', {
        'form': form,
        'form_action': reverse('petOwner:create_login'),
    })

def create_login(req):
    if not req.POST:
        raise Http404()
    
    POST = req.POST
    form = LoginForm(POST)
    
    if form.is_valid():
        authenticated_user = authenticate(
            username = form.cleaned_data.get('username', ''),
            password = form.cleaned_data.get('password', ''),
        )
        
        if authenticated_user and authenticated_user is not None:
            messages.success(req, 'You are logged.')
            login(req, authenticated_user)
        
        else:
            messages.error(req, 'Invalid credentials.')
            
    else:
        messages.error(req, 'Invalid form.')
        
    
        
    return redirect(reverse('petOwner:login'))
    

