from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Type, Challange



def TypeListView(ListView):
    """ State property list view """
    model = EstateProperty
    template_name = "app_projects/properties/index.html"
    ordering = "name"
