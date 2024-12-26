from django.http import HttpResponse
from django.template import loader

def login(request):
  template = loader.get_template('login.html')
  context = {
    'firstname': 'Linus',
  }
  return HttpResponse(template.render(context, request))