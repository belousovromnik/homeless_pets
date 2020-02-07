from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .models import Pet


class AboutPageView(TemplateView):
    template_name='about.html'


class PetListView(ListView):
    model=Pet


class PetView(DetailView):
    model=Pet


class ContactsView(TemplateView):
    template_name='contacts.html'