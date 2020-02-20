from django.urls import path

from simple_visualization.views import Graph

urlpatterns = [
    path('', Graph.as_view(), name='index'),
]