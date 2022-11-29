from django.http import HttpResponse
from .models import clases, avatar 
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from .forms import UserEditForm, UsearRegisterForm

class clasesList(ListView):
    model = clases
    template_name = "clases.html"
    context_object_name = "clases"

class clasesedit(ListView):
    model = clases
    template_name = "clasesedit.html"
    context_object_name = "clases"



class clasesDetailView(DetailView):
    model = clases
    template_name = "clasesdetail.html"
    context_object_name = "clases"



class clasesCreateView(CreateView):
    model = clases
    template_name = "clasescreate.html"
    fields = ["nombre", "publico"]
    success_url = '/AppCS/'


class clasesUpdateView(UpdateView):
    model = clases
    template_name = "clasesupdate.html"
    fields = ('__all__')
    success_url = '/AppCS/'


class clasesDeleteView(DeleteView):
    model = clases
    template_name = "clasesdelete.html"
    success_url = '/AppCS/'






def inicio(request):
    

    return render(request, 'inicio.html')

def profesores(request):

    return render(request, 'profesores.html')

def sobre(request):
    
    return render(request, 'sobre.html')

def contacto(request):
    
    return render(request, 'contacto.html')

def loginView(request):
    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':
        miFormulario = AuthenticationForm(request, data=request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username = usuario, password = psw)

            if user:
                login(request, user)
                return render(request, "inicio.html")
            
            else:
                return render(request, "inicio.html")
       
        return render(request, "inicio.html", {'mensaje': f"ingrese un usuario valido"})

    else:
        miFormulario = AuthenticationForm()
        return render(request, 'login.html', {"miFormulario": miFormulario})


def register(request):
    
    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = UsearRegisterForm(request.POST)

        if miFormulario.is_valid():

            username = miFormulario.cleaned_data["username"]
            miFormulario.save()
            return render(request, "inicio.html", {"mensaje": f'El usuario {username} fue creado con exito. Recuerde para ingresar'})
        else:
            return render(request, "inicio.html", {"mensaje": f'No fue posible crear el usuario'})
            
    else:
        miFormulario = UsearRegisterForm()
        return render(request, 'register.html', {"miFormulario": miFormulario})


def edituser(request):

    print('method:', request.method)
    print('post:', request.POST)

    usuario = request.user 

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]  
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])

            usuario.save()

            return render(request, "inicio.html")
        return render(request, "editUser.html")
    else:
        miFormulario = UserEditForm(instance=request.user)
        return render(request, "editUser.html", {"miFormulario": miFormulario})


