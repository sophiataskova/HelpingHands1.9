from django.shortcuts import render

import json

# might not need all of these imports
from django.shortcuts import render_to_response, render, get_object_or_404

from django.template import RequestContext, loader

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login

from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.contrib.auth.models import User

from django.contrib.auth import authenticate
from django.db.utils import IntegrityError

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

from helping_hands_app.models import ITUUser, ITUUserManager, NGOUser


def index(request):
    return HttpResponse("Hello, world. You're at the events index.")


def helping_hands_register(request):
    if request.method == 'POST':
        
    	# import pdb; pdb.set_trace()
        try:
            itu_user = ITUUser.objects.create_user(
                request.POST['username'],                
                request.POST['email'],                
                request.POST['first_name'],
                request.POST['last_name'],
                request.POST['security_question'],
                request.POST['security_answer'],
                request.POST['gender'],
                request.POST['phone_number'],
                request.POST['password'],
                )            
            itu_user.save()
            
            return HttpResponseRedirect('/admin/')

        except IntegrityError:
            # Duplicate entry - I probably should have checked for this before making a save! 
            response_data = {}
            response_data['result'] = 'error'
            response_data['message'] = 'Username already exists'
            return HttpResponseBadRequest(json.dumps(response_data), content_type="application/json")


def helping_hands_login(request):
    
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    security_question = request.POST['security_question']
    security_answer = request.POST['security_answer']
    gender = request.POST['gender']
    phone_number = request.POST['phone_number']
                
    user = authenticate(email=email, password=password)   
    import pdb; pdb.set_trace()
    if user is not None:
        login(request, user)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def helping_hands_logout(request):
    logout(request)    
    return HttpResponse(status=200)