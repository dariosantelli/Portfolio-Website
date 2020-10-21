from django.shortcuts import render
from django.http import HttpResponse

"""
def home(request):
    return HttpResponse('Hello, World!')
"""
def portfolio(request):
    """
    template = loader.get_template('portfolio/index.html')
    """

    template_name = 'portfolio/index.html'

    return HttpResponse(render(request, template_name))
