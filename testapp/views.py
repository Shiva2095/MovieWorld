from django.shortcuts import render,redirect
from testapp.models import Movie
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.
class CompanyListView(ListView):
    model = Movie

class CompanyDetailView(DetailView):
    model = Movie

class CompanyCreateView(CreateView):
    model = Movie
    fields = ('rdate','movien','hero','heroin','rating')

class CompanyUpdateView(UpdateView):
    model = Movie
    fields = ('rdate','movien','hero','heroin','rating')

class CompanyDeleteView(DeleteView):
    model = Movie
    success_url=reverse_lazy('movies')
