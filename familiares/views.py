from django.shortcuts import render

# Create your views here.
def mostrar_familia(request):

    return render(request, 'familia.html', context={})