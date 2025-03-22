from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Alumno


#-----ALTAS-----------
class CrearAlumno(SuccessMessageMixin, CreateView):
    model = Alumno
    fields = "__all__"
    success_message = "Alumno agregado correctamente"
    success_url = reverse_lazy('listar')  # Redirige a la lista de alumnos

#-----BAJAS-----------
class EliminarAlumno(SuccessMessageMixin, DeleteView):
    model = Alumno
    success_message = "Alumno eliminado correctamente"

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('listar')

#-----CAMBIOS-----------
class ActualizarAlumno(SuccessMessageMixin, UpdateView):
    model = Alumno
    fields = "__all__"
    success_message = "Alumno actualizado correctamente"

    def get_success_url(self):
        return reverse('listar')

#-----CONSULTAR TODOS
class ListarAlumnos(ListView):
    model = Alumno

#----CONSULTAR UN ALUMNO
class DetalleAlumno(DetailView):
    model = Alumno

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = "alumnos/login.html"