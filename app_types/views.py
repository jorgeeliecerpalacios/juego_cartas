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


class ChallengeListView(ListView):
    """ State property list view """
    # return HttpResponse('hola mundo')
    model = Challange
    template_name = "challenge/challenge.html"
    ordering = "name"
    context_object_name = "challenge"

    def get_queryset(self):

        type_id = self.kwargs.get('type_id')
        print("type_id", type_id)
        # super().get_queryset().filter(types_id=type_id)
        return Challange.objects.filter(types_id=type_id)