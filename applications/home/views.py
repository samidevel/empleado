from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm

class CssPrueba(TemplateView):
    template_name = 'home/prueba.html'


class ResumenFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'




class IndexView(TemplateView):
    template_name = 'home/home.html'


class PruebaListView(ListView):
    template_name='home/lista.html'
    queryset=['a','b','c']
    context_object_name= 'lista_prueba'



class ModeloPruebaView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name= 'lista_prueba'


class PruebaCreateView(CreateView):

    template_name = 'home/add.html'
    model = Prueba
    form_class = PruebaForm
    #fields = '__all__'
    success_url = '/'