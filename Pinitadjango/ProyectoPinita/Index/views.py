from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, 'index.html')

def Fundacion(request):
    return render(request,'Fundacion.html')

def formlogin(request):
    return render(request, 'formlogin.html')

def registro(request):
    return render(request, 'registro.html')

def controlBlog(request):
    return render(request, 'controlBlog.html')

def contacto(request):
    return render(request, 'contacto.html')

def single(request):
    return render(request, 'single.html')