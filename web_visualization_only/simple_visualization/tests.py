from django.test import TestCase
from simple_visualization.views import Graph
from django.test import Client
import logging

# Create your tests here.
class TestSimpleVisualizationGraph(TestCase):
    def test_template(self):
        client = Client()
        response = client.get('')
        logging.error(f'got it {response}')