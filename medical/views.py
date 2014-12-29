#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the Medical Info index.")
	
def home(request):
   context = RequestContext(request,
                           {'user': request.user})
   return render_to_response('templates/admin/home.html',
                             context_instance=context)
