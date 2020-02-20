from django.shortcuts import render
from simple_visualization.visual_helper import graphics
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

class Graph(TemplateView):
    template_name = 'simple_visualization/index.html'

    def get_context_data(self, **kwargs):
        context = super(Graph, self).get_context_data(**kwargs)

        heatmap, scatter, data_indexes = graphics()
        
        
        context['heatmap'] = heatmap
        context['scatter'] = scatter
        context['data_indexes'] = data_indexes

        return context