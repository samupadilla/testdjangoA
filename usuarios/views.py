from django.http import HttpRequest
from django.shortcuts import render
from . models import Aprendiz
from . forms import FormularioAprendiz

#from Models.Aprendiz.forms import FormularioAlumno

# Create your views here.
# def usuariolist(request):
#     return render(request,'usuariolist.html')

class FormularioAprendizView(HttpRequest):
    def index(request):
        aprendiz=FormularioAprendiz()
        return render(request,"AprendizHome.html",{"form":aprendiz})

    def procesar_formulario(request):
        aprendiz=FormularioAprendiz(request.POST, request.FILES)
        #aprendiz=FormularioAprendiz(request.POST)
        if aprendiz.is_valid():
            aprendiz.save()
            aprendiz=FormularioAprendiz()
        return render(request,"AprendizHome.html",{"form":aprendiz,"mesaje":"ok"})
    
    def edit(request,id_aprendiz):
        aprendiz=Aprendiz.objects.filter(id=id_aprendiz).first()
        form=FormularioAprendiz(instance=aprendiz)
        return render(request, "AprendizEdit.html",{"form":form,"aprendiz":aprendiz})

    def actualizar_aprendiz(request,id_aprendiz):
        aprendiz=Aprendiz.objects.get(pk=id_aprendiz)
        form=FormularioAprendiz(request.POST,instance=aprendiz)
        if form.is_valid():
            form.save()
        aprendices=Aprendiz.objects.all()
        return render(request,"usuariolist.html",{"get_aprendices":aprendices})

    def eliminar_aprendiz(request, id_aprendiz):
        aprendiz=Aprendiz.objects.get(pk=id_aprendiz)
        aprendiz.delete()
        aprendices=Aprendiz.objects.all()
        return render(request, "usuarioList.html",{"get_aprendices":aprendices})




def usuariolist(request):
    get_aprendices=Aprendiz.objects.all()
    data={
        'get_aprendices':get_aprendices
    }
    return render(request,'usuariolist.html', data)


