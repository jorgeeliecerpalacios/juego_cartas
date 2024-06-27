from django.shortcuts import render, HttpResponse


# Create your views here.
from django.views.generic.list import ListView
from .models import Type, Challange


class TypeListView(ListView):
    """ State property list view """
    # return HttpResponse('hola mundo')
    model = Type
    template_name = "types/type.html"
    ordering = "name"
    context_object_name = "type"
