from django.shortcuts import render
from django.views.generic import TemplateView
# helloworld is a templateview
class HelloWorld(TemplateView):
    template_name = 'test.html'






# Create your views here.
