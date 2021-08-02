from django import forms
from django.shortcuts import redirect, render
from .models import Persona
from .forms import PersonaForm
# Create your views here.

def inicio(request):
    personas = Persona.objects.all()
    contexto = {
        'personas' : personas
    }
    return render(request, 'index.html',contexto)

def nuevo(request):
    if request == 'GET':
        form = PersonaForm()
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'nuevo.html', contexto)

def editar(request,id):
    persona = Persona.objects.get(id=id)
    if request.method == 'GET':
        form = PersonaForm(instance=persona)
        contexto = {
            'form' : form
        }
    else:
        form = PersonaForm(request.POST, instance=persona)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'nuevo.html',contexto)

def eliminar(request,id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    return redirect('index')
