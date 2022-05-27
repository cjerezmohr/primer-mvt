from django.shortcuts import render

# Create your views here.
def mostrar_familia(request):

    context = {
        'nombre':'jimmy',
        'apellido':'mohr'
    }
    return render(request, 'familia.html', context= context)