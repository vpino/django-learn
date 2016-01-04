# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from apis.models import PackageGeneric, PackageGenericEdu, PackageCinnamon, PackageCinnamonEdu, PackageMate, PackageMateEdu
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from  apis.form import PackageGenericForm, PackageGenericEduForm, PackageCinnamonForm, PackageCinnamonEduForm, PackageMateForm, PackageMateEduForm
from django.contrib import messages

#Vista que retorna todos los paquetes genericos
def package_generic(request):

    #Guardamos en el objeto Generic todos los paquetes
    generic = PackageGeneric.objects.all()


    msj = messages.add_message(request, messages.INFO, 'Hello world.')
    msj = messages.debug(request, '%s SQL statements were executed.' )
    msj = messages.info(request, 'Three credits remain in your account.')
    msj= messages.success(request, 'Profile details updated.')
    msj = messages.warning(request, 'Your account expires in three days.')
    msj = messages.error(request, 'Document deleted')

    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('apis/PackageGeneric.html',
                                {'generic': generic, 'messages': msj})

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

    #Retornamos al template generic_create.html y le pasamos el formulario instanciado
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
            return redirect('generic')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageGenericForm y le mostramos el registro
        #capturado con el metodo get_object_or_404
        form = PackageGenericForm(instance=package)

    #Retornamos al template gereric_edit.html y le pasamos el formulario instanciado
    return render_to_response('apis/generic_edit.html', {'form': form},
                              context_instance=RequestContext(request))

#Vista que retorna todos los paquetes genericos  educativos
def package_generic_edu(request):

    #Guardamos en el objeto Generic todos los paquetes genericos educativos
    generic = PackageGenericEdu.objects.all()

    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('apis/PackageGenericEdu.html',
                                {'generic': generic})

#Metodo para añadir un paquete a la lista de paquetes genericos educativos
def generic_edu_create(request):
    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Instanciamos un objeto de tipo PackageGenericEduForm y le pasamos como parametros los elementos
        #que enviaron por el formulario y lo guardamos en un objeto
        form = PackageGenericEduForm(request.POST)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():
            #Si usamos ModelForm si pasa las validaciones simplemente le decimos que
            # lo inserte en la base de datos con form.save() ya el metodo hace la instancia por si solo
            # del modelo pasado y lo inserta
            form.save()

            #retornamos a la vista de paquetes educativos
            return redirect('generic_edu')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageGenericEdu
        form = PackageGenericEduForm()

    #Retornamos al template generic_edu_create.html y le pasamos el formulario instanciado
    return render_to_response('apis/generic_edu_create.html', {'form': form},
                              context_instance=RequestContext(request))

#View para modificar un paquete generic educativo
def generic_edu_edit(request, package_id):
    #Usamos el metodo get_object_or_404 donde le pasamos 2 parametos el objeto del modelo y un id
    # lo guardamos en un objeto, y si no existe retornamos a la pagina de error 404
    package = get_object_or_404(PackageGenericEdu, pk=package_id)

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Le pasamos los datos del form mas la instancia del objeto capturado en el metodo get_object_or_404
        form = PackageGenericEduForm(request.POST, instance=package)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():

            #Insertamos en el base de datos el registro actualizado
            form.save()

            #retornamos a la vista generic_edu que tiene la lista de paquetes y le pasamos el id
            return redirect('generic_edu')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageGenericEduForm y le mostramos el registro
        #capturado con el metodo get_object_or_404
        form = PackageGenericEduForm(instance=package)

    #Retornamos al template generic_edu_edit.html y le pasamos el formulario instanciado
    return render_to_response('apis/generic_edu_edit.html', {'form': form},
                              context_instance=RequestContext(request))

#Vista que retorna todos los paquetes de Cinnamon
def package_cinnamon(request):

    #Guardamos en el objeto cinnamon todos los paquetes de cinnamon
    cinnamon = PackageCinnamon.objects.all()

    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('apis/package_cinnamon.html',
                                {'cinnamon': cinnamon})

#View para añadir un paquete de la lista de cinnamon
def package_cinnamon_create(request):

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Instanciamos un objeto form de tipo PackageGeneric y le pasamos como parametros los elementos
        #que enviaron por el formulario y lo guardamos en un objeto
        form = PackageCinnamonForm(request.POST)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():
            #Si usamos ModelForm si pasa las validaciones simplemente le decimos que
            # lo inserte en la base de datos con form.save() ya el metodo hace la instancia por si solo
            # del modelo pasado y lo inserta
            form.save()

            #retornamos a la view de paquetes Cinnamon
            return redirect('package_cinnamon')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto form  de tipo PackageCinnamonForm
        form = PackageCinnamonForm()

        return render_to_response('apis/package_cinnamon_create.html', {'form': form},
                                  context_instance=RequestContext(request))

#View para editar un paquete de la lista de cinnamon
def package_cinnamon_edit(request, package_id):
    #Usamos el metodo get_object_or_404 donde le pasamos 2 parametos el objeto del modelo y un id
    # lo guardamos en un objeto, y si no existe retornamos a la pagina de error 404
    package = get_object_or_404(PackageCinnamon, pk=package_id)

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Le pasamos los datos del form mas la instancia del objeto capturado en el metodo get_object_or_404
        form = PackageCinnamonForm(request.POST, instance=package)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():

            #Insertamos en el base de datos el registro actualizado
            form.save()

            #retornamos a la vista package_cinnamon que tiene la lista de paquetes
            return redirect('package_cinnamon')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageCinnamonForm y le mostramos el registro
        #capturado con el metodo get_object_or_404
        form = PackageCinnamonForm(instance=package)

    #Retornamos al template generic_edu_edit.html y le pasamos el formulario instanciado
    return render_to_response('apis/package_cinnamon_edit.html', {'form': form},
                              context_instance=RequestContext(request))



#Vista que retorna todos los paquetes de cinnamon educativo
def package_cinnamon_edu(request):

    #Guardamos en el objeto cinnamon todos los paquetes de cinnamon educativo
    cinnamon = PackageCinnamonEdu.objects.all()

    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('apis/package_cinnamon_edu.html',
                                {'cinnamon': cinnamon})

#View para añadir un paquete a la lista de cinnamon educativo
def package_cinnamon_edu_create(request):

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Instanciamos un objeto form de tipo PackageCinnamonEduForm y le pasamos como parametros los elementos
        #que enviaron por el formulario y lo guardamos en un objeto
        form = PackageCinnamonEduForm(request.POST)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():
            #Si usamos ModelForm si pasa las validaciones simplemente le decimos que
            # lo inserte en la base de datos con form.save() ya el metodo hace la instancia por si solo
            # del modelo pasado y lo inserta
            form.save()

            #retornamos a la view de paquetes Cinnamon
            return redirect('package_cinnamon_edu')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto form  de tipo PackageCinnamonEduForm
        form = PackageCinnamonEduForm()

        return render_to_response('apis/package_cinnamon_edu_create.html', {'form': form},
                                  context_instance=RequestContext(request))

#View para editar un paquete de la lista de cinnamon educativo
def package_cinnamon_edu_edit(request, package_id):

    #Usamos el metodo get_object_or_404 donde le pasamos 2 parametos el objeto del modelo y un id
    # lo guardamos en un objeto, y si no existe retornamos a la pagina de error 404
    package = get_object_or_404(PackageCinnamonEdu, pk=package_id)

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Le pasamos los datos del form mas la instancia del objeto capturado en el metodo get_object_or_404
        form = PackageCinnamonEduForm(request.POST, instance=package)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():

            #Insertamos en el base de datos el registro actualizado
            form.save()

            #retornamos a la vista package_cinnamon que tiene la lista de paquetes
            return redirect('package_cinnamon_edu')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageCinnamonForm y le mostramos el registro
        #capturado con el metodo get_object_or_404
        form = PackageCinnamonEduForm(instance=package)

    #Retornamos al template generic_edu_edit.html y le pasamos el formulario instanciado
    return render_to_response('apis/package_cinnamon_edu_edit.html', {'form': form},
                              context_instance=RequestContext(request))



#Vista que retorna todos los paquetes de mate
def package_mate(request):

    #Guardamos en el objeto mate todos los paquetes
    mate = PackageMate.objects.all()

    #Retornamos a el templates y le pasamos todos los paquetes
    return render_to_response('apis/package_mate.html',
                                {'mate': mate})

#View para añadir un nuevo paquete a la lista de mate
def package_mate_create(request):

    #Validamos si el form fue enviado por POST
    if request.method == 'POST':

        #Instanciamos un objeto form de tipo PackageMateForm y le pasamos como parametros los elementos
        #que enviaron por el formulario y lo guardamos en un objeto
        form = PackageMateForm(request.POST)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():
            #Si usamos ModelForm si pasa las validaciones simplemente le decimos que
            # lo inserte en la base de datos con form.save() ya el metodo hace la instancia por si solo
            # del modelo pasado y lo inserta
            form.save()

            #retornamos a la view de paquetes Cinnamon
            return redirect('package_mate')
    else:

        #Instaciamos un objeto form  de tipo PackageMateForm
        form = PackageMateForm()

        return  render_to_response('apis/package_mate_create.html', {'form': form},
                                   context_instance=RequestContext(request))

#View para editar un paquete de la lista de mate
def package_mate_edit(request, package_id):

    #Usamos el metodo get_object_or_404 donde le pasamos 2 parametos el objeto del modelo y un id
    # lo guardamos en un objeto, y si no existe retornamos a la pagina de error 404
    package = get_object_or_404(PackageMate, pk=package_id)

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Le pasamos los datos del form mas la instancia del objeto capturado en el metodo get_object_or_404
        form = PackageMateForm(request.POST, instance=package)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():

            #Insertamos en el base de datos el registro actualizado
            form.save()

            #retornamos a la vista package_cinnamon que tiene la lista de paquetes
            return redirect('package_mate')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageMateForm y le mostramos el registro
        #capturado con el metodo get_object_or_404
        form = PackageMateForm(instance=package)

    #Retornamos al template generic_edu_edit.html y le pasamos el formulario instanciado
    return render_to_response('apis/package_mate_edit.html', {'form': form},
                              context_instance=RequestContext(request))

#Vista que retorna todos los paquetes de mate educativos
def package_mate_edu(request):

    #Guardamos en el objeto mate todos los paquetes educativos de mate
    mate = PackageMateEdu.objects.all()

    #Retornamos a el templates y le pasamos todas los paquetes
    return render_to_response('apis/package_mate_edu.html',
                                {'mate': mate})

#View para añadir un nuevo paquete a la lista de mate educativo
def package_mate_edu_create(request):

    #Validamos si el form fue enviado por POST
    if request.method == 'POST':

        #Instanciamos un objeto form de tipo PackageMateEduForm y le pasamos como parametros los elementos
        #que enviaron por el formulario y lo guardamos en un objeto
        form = PackageMateEduForm(request.POST)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():
            #Si usamos ModelForm si pasa las validaciones simplemente le decimos que
            # lo inserte en la base de datos con form.save() ya el metodo hace la instancia por si solo
            # del modelo pasado y lo inserta
            form.save()

            #retornamos a la view de paquetes Cinnamon
            return redirect('package_mate_edu')
    else:

        #Instaciamos un objeto form  de tipo PackageMateEduForm
        form = PackageMateEduForm()

        return  render_to_response('apis/package_mate_edu_create.html', {'form': form},
                                   context_instance=RequestContext(request))

#View para editar un paquete de la lista de mate educativo
def package_mate_edu_edit(request, package_id):

    #Usamos el metodo get_object_or_404 donde le pasamos 2 parametos el objeto del modelo y un id
    # lo guardamos en un objeto, y si no existe retornamos a la pagina de error 404
    package = get_object_or_404(PackageMateEdu, pk=package_id)

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Le pasamos los datos del form mas la instancia del objeto capturado en el metodo get_object_or_404
        form = PackageMateEduForm(request.POST, instance=package)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():

            #Insertamos en el base de datos el registro actualizado
            form.save()

            #retornamos a la vista package_cinnamon que tiene la lista de paquetes
            return redirect('package_mate_edu')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo PackageMateForm y le mostramos el registro
        #capturado con el metodo get_object_or_404
        form = PackageMateForm(instance=package)

    #Retornamos al template generic_edu_edit.html y le pasamos el formulario instanciado
    return render_to_response('apis/package_mate_edu_edit.html', {'form': form},
                              context_instance=RequestContext(request))