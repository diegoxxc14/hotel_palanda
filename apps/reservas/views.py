from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.
''' HABITACIÓN'''
@login_required
def listar_habitaciones(request, template_name='reservas/listar_habitaciones.html'):
    lista_habs = Habitacion.objects.all()
    return render(request, template_name, {'habitaciones':lista_habs})

@method_decorator(login_required, name='dispatch')
class CrearHabitacion(CreateView):
    model = Habitacion
    #fields = ['numero', 'tipo', 'precio', 'planta', 'activa', 'detalles']
    fields = '__all__'
    template_name_suffix = '_crear'
    success_url = reverse_lazy('reservas:listar_hab')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Habitación creada correctamente.')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditarHabitacion(UpdateView):
    model = Habitacion
    #fields = ['numero', 'tipo', 'precio', 'planta', 'activa', 'detalles']
    fields = '__all__'
    template_name_suffix = '_editar'
    success_url = reverse_lazy('reservas:listar_hab')

    def form_valid(self, form):
        #data_form = form.cleaned_data #Datos del formulario
        #if not data_form['activa']: #Si se quiere desactivar
        hab_pk = self.kwargs['pk']
        existe = Reservacion.objects.filter(habitacion=hab_pk, estado__in=['PC','CF','EE']).exists()
        if existe: #Si existe una reserva activa con esta habitación
            messages.add_message(self.request, messages.WARNING, 'Esta habitación no se puede editar.')
            return super().form_invalid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Habitación modificada correctamente.')
        return super().form_valid(form)       

''' DETALLES HABITACIÓN'''
@login_required
def listar_detallesHab(request, template_name='reservas/listar_detallesHab.html'):
    detallesHab = DetalleHabitacion.objects.all()
    return render(request, template_name, {'detallesHab':detallesHab})

@method_decorator(login_required, name='dispatch')
class CrearDetalleHabitacion(CreateView):
    model = DetalleHabitacion
    fields = '__all__'
    template_name_suffix = '_crear'
    success_url = reverse_lazy('reservas:listar_detHab')

''' SERVICIO '''
@login_required
def listar_servicios(request, template_name='reservas/listar_servicios.html'):
    servicios = Servicio.objects.all()
    return render(request, template_name, {'servicios':servicios})

@method_decorator(login_required, name='dispatch')
class CrearServicio(CreateView):
    model = Servicio
    fields = '__all__'
    template_name_suffix = '_crear'
    success_url = reverse_lazy('reservas:listar_ser')

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Servicio creado correctamente.')
        return super().form_valid(form)