from django.shortcuts import render

# Create your views here.
def listar_Noticias(request):
    return render(request, 'noticias/listar.html')
