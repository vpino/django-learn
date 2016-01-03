from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from apis.models import PackageGeneric, PackageGenericEdu, PackageCinnamon, PackageCinnamonEdu, PackageMate, PackageMateEdu
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from  apis.form import PackageGenericForm

#Vista que retorna todos los paquetes genericos
def package_generic(request):

    #Guardamos en el objeto Generic todos los paquetes
    generic = PackageGeneric.objects.all()

    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('apis/PackageGeneric.html',
                                {'generic': generic})

def generic_create(request):
    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Instanciamos un objeto de tipo PackageGeneric y le pasamos como parametros los elementos
        #que enviaron por el formulario y lo guardamos en un objeto
        form = PackageGenericForm(request.POST)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():
            #Si usamos ModelForm si pasa las validaciones simplemente le decimos que
            # lo inserte en la base de datos con form.save() ya el metodo hace la instancia por si solo
            # del modelo pasado y lo inserta
            form.save()

            #retornamos a la vista de preguntas
            return redirect('generic')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageGeneric
        form = PackageGenericForm()

    #Retornamos al template question_create.html y le pasamos el formulario instanciado
    return render_to_response('apis/generic_create.html', {'form': form},
                              context_instance=RequestContext(request))

#View para modificar un paquete generic
def generic_edit(request, package_id):
    #Usamos el metodo get_object_or_404 donde le pasamos 2 parametos el objeto del modelo y un id
    # lo guardamos en un objeto, y si no existe retornamos a la pagina de error 404
    package = get_object_or_404(PackageGeneric, pk=package_id)

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Le pasamos los datos del form mas la instancia del objeto capturado en el metodo get_object_or_404
        form = PackageGenericForm(request.POST, instance=package)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():

            #Insertamos en el base de datos el registro actualizado
            form.save()

            #retornamos a la vista generic que tiene la lista de paquetes y le pasamos el id
            return redirect('generic', package_id)

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageGenericForm y le mostramos el registro
        #capturado con el metodo get_object_or_404
        form = PackageGenericForm(instance=package)

    #Retornamos al template gereric_edit.html y le pasamos el formulario instanciado
    return render_to_response('apis/generic_edit.html', {'form': form},
                              context_instance=RequestContext(request))

#Vista que retorna todos los paquetes genericos  educativos
def PackageGenericEdu(request):

    #Guardamos en el objeto Generic todos los paquetes genericos educativos
    generic = PackageGenericEdu.objects.all()

    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('apis/PackageGenericEdu.html',
                                {'generic': generic})

#Vista que retorna todos los paquetes de Cinnamon
def PackageCinnamon(request):

    #Guardamos en el objeto cinnamon todos los paquetes de cinnamon
    cinnamon = PackageCinnamon.objects.all()

    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('apis/PackageCinnamon.html',
                                {'cinnamon': cinnamon})

#Vista que retorna todos los paquetes de cinnamon educativo
def PackageCinnamonEdu(request):

    #Guardamos en el objeto cinnamon todos los paquetes de cinnamon educativo
    cinnamon = PackageCinnamonEdu.objects.all()

    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('apis/PackageCinnamonEdu.html',
                                {'cinnamon': cinnamon})

#Vista que retorna todos los paquetes de mate
def PackageMate(request):

    #Guardamos en el objeto Generic todos los paquetes
    mate = PackageMate.objects.all()

    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('apis/PackageMate.html',
                                {'mate': mate})

#Vista que retorna todos los paquetes de mate educativos
def PackageMateEdu(request):

    #Guardamos en el objeto mate todos los paquetes educativos de mate
    mate = PackageGeneric.objects.all()

    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('apis/PackageMateEdu.html',
                                {'mate': mate})

