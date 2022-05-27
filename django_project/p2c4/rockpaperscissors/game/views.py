from django.http import HttpResponse
from django.template import loader



def index(request):
    template = loader.get_template('index')
    return HttpResponse(template.render(request=request))

def goodbye(request):
    template = loader.get_template('goodbye.html')
    return HttpResponse(template.render(request=request))

