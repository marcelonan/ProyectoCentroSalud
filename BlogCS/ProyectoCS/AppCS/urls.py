
from django.urls import path
from .views import  inicio, profesores, sobre, contacto, clasesList, clasesDetailView, clasesCreateView, clasesedit, clasesUpdateView, clasesDeleteView, loginView, register, edituser
from AppCS import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    
    path('', views.inicio, name="Inicio"),
    path('profesores', views.profesores, name="Profesores"),
    path('sobre', views.sobre, name="Sobre"),
    path('contacto', views.contacto, name="Contacto"),
    path('clases', clasesList.as_view(), name="Clases"),
    path('clasesedit', clasesedit.as_view(), name="editclases"),

    path('clasesdetalle/<pk>', clasesDetailView.as_view(), name="Clasesdetail"),
    path('clasescrear/', clasesCreateView.as_view(), name="createclases"),
    path('clasesupdate/<pk>', clasesUpdateView.as_view(), name="updateclases"),
    path('clasesdelete/<pk>', clasesDeleteView.as_view(), name="deleteclases"),
    path('login', views.loginView, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path('editUser', views.edituser, name="userEdit"),













]
