from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home (request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def curriculumvitae(request):
    template = loader.get_template('curriculumvitae.html')
    return HttpResponse(template.render())
def latihan_django2 (request):
    template = loader.get_template('latihan_django2.html')
    return HttpResponse(template.render())
def depan(request):
    template = loader.get_template('depan.html')
    return HttpResponse(template.render())
def biodata(request):
    template = loader.get_template('biodata.html')
    return HttpResponse(template.render())
def History(request):
    template = loader.get_template('History.html')
    return HttpResponse(template.render())
def cerita(request):
    template = loader.get_template('cerita.html')
    return HttpResponse(template.render())
def aboutme(request):
    template = loader.get_template('aboutme.html')
    return HttpResponse(template.render())



