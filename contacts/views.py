# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact
# Create your views here.
class ContactList(ListView): 
    model = Contact
class ContactDetail(DetailView): 
    model = Contact
class ContactCreate(CreateView):
    fields='__all__'
    model = Contact
class ContactUpdate(UpdateView): 
    fields='__all__'
    model = Contact        
class ContactDelete(DeleteView): 
    model = Contact    
    success_url = reverse_lazy('contacts:list')    