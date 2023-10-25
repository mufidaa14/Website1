from django.urls import path
from . import views

urlpatterns = [
    path("latihan_django2/", views.latihan_django2, name="latihan_django2"),
    path("depan/", views.depan, name="depan"),
    path("biodata/", views.biodata, name="biodata"),
    path("History/", views.History, name="History"),
    path("home/", views.home, name="home"),
    path("curriculumvitae/", views.curriculumvitae, name="curriculumvitae"),
    path("cerita/", views.cerita, name="cerita"),
    path("aboutme/", views.aboutme, name="aboutme"),
    
]