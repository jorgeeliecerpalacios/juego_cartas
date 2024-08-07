# urls app_types

from django.urls import path

# Views

from . import views

urlpatterns = [
    path(
    route='',
    view=views.TypeListView.as_view(),
    name='types'
    ),

    path(
    route='challenge/<int:type_id>/',
    view=views.ChallengeListView.as_view(),
    name='challenges'
    ),
]