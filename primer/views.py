from django.shortcuts import render

from primer.models import Cake


# Create your views here.

def index(request):
    cakes = Cake.objects.all()
    return render(request, 'index.html', context={'cakes': cakes})
