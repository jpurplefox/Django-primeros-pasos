from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from bandas.models import Banda

# Create your views here.
class BandaList(ListView):
    model = Banda
    context_object_name = 'bandas'

class BandaDetail(DetailView):
    model = Banda
    context_object_name = 'banda'

class BandaCreate(CreateView):
    model = Banda
    fields = ['nombre', 'fundacion', 'genero', 'origen']

class BandaUpdate(UpdateView):
    model = Banda
    fields = ['nombre', 'fundacion', 'genero', 'origen']

class BandaDelete(DeleteView):
    model = Banda
    context_object_name = 'banda'
    success_url = reverse_lazy('banda-list')
