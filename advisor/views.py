# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.template import Context, loader, RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.mail import EmailMessage

import datetime, math

from django import forms

from django.forms import ModelForm

from advisor.models import *

class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.title

class q2a_form(forms.Form):
	answer = MyModelChoiceField(queryset=Socs.objects.all())

def page(request):

    return render_to_response('page.html', {}, context_instance=RequestContext(request))
    
def q1(request):
    #Test DB Model
    
    #socs_list = Socs.objects.all()

    return render_to_response('q1.html', {}, context_instance=RequestContext(request))
    
def q2a(request):
    the_form = q2a_form()
    
    socs_list = Socs.objects.all()

    return render_to_response('q2-a.html', {'the_form':the_form}, context_instance=RequestContext(request))
    
def q2aResponse(request):
    if request.method == "POST":
            form_input = q2a_form(request.POST)
            
            #clear values
            answer_string = ""
            success = False
    
            if form_input.is_valid():
                success = True
                answer_string = form_input.cleaned_data['answer']
                
                
                #Search DB for Career choices
                
                socs_list = Socs.objects.filter(title=answer_string)

                return render_to_response('q2-a-response.html', {'answer_string':answer_string}, context_instance=RequestContext(request))
                
def q2b(request):

    return render_to_response('q2-b.html', {}, context_instance=RequestContext(request))
    
def q3a(request):

   #search DB for Nesscary jobs
   
   ess_list = Ess.objects.filter(reliability=3)

   return render_to_response('q3-a.html', {'ess_list':ess_list}, context_instance=RequestContext(request))
    
def q3b(request):

    return render_to_response('q3-b.html', {}, context_instance=RequestContext(request))
    
def q3bResponse(request):

    return render_to_response('q3-b-response.html', {}, context_instance=RequestContext(request))
    
def result(request):

    return render_to_response('result.html', {}, context_instance=RequestContext(request))