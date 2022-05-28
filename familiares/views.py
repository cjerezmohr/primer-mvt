from django.shortcuts import render
from familiares.models import Familia


# Create your views here.
def mostrar_familia(request):

    familiar = Familia.objects.all()

    context = {
    'familiar': familiar
    }
    return render(request, 'familia.html', context)