from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from askquestions.models import Question
from django.template import RequestContext
from  askquestions.form import QuestionForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):

    #Guardamos en el objeto questions todas las preguntas
    questions = Question.objects.all()

    #Retornamos a el templates y le pasamos todas las preguntas
    return render_to_response('askquestions/index.html',
                                {'question': questions})

@login_required()
def question_detail(request, question_id):

    #Con el metodo get_object le pasamos como parametro una pregunta y el id de dicha pregunta
    #si el id pasado no existe, retorna el error 404
    question = get_object_or_404(Question, pk=question_id)

    #Retornamos a la template question_detail y le pasamos como para la pregunta encontrada
    return render_to_response('askquestions/question_detail.html', {'question': question})

@login_required()
def question_create(request):
    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Instanciamos un objeto de tipo QuestionForm y le pasamos como parametros los elementos
        #que enviaron por el formulario y lo guardamos en un objeto
        form = QuestionForm(request.POST)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():

            #Instanciamos un objeto de tipo Question y lo llenamos con los datos enviados
            #Manera con Form
            #question = Question(asunto = form.cleaned_data['subject'],
                                #descripcion = form.cleaned_data['description'],
                                #fecha_publicacion = timezone.now())

            #Lo insertamos en la base de datos
            #question.save()

            #Si usamos ModelForm si pasa las validaciones simplemente le decimos que
            # lo inserte en la base de datos con form.save() ya el metodo hace la instancia por si solo
            # del modelo pasado y lo inserta
            form.save()

            #retornamos a la vista de preguntas
            return redirect('questions')

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo QuestionForm
        form = QuestionForm()

    #Retornamos al template question_create.html y le pasamos el formulario instanciado
    return render_to_response('askquestions/question_create.html', {'form': form},
                              context_instance=RequestContext(request))

@login_required()
def question_edit(request, question_id):
    #Usamos el metodo get_object_or_404 donde le pasamos 2 parametos el objeto del modelo y un id
    # lo guardamos en un objeto, y si no existe retornamos a la pagina de error 404
    question = get_object_or_404(Question, pk=question_id)

    #Si el metodo enviado por el formulario es POST
    if request.method == 'POST':

        #Le pasamos los datos del form mas la instancia del objeto capturado en el metodo get_object_or_404
        form = QuestionForm(request.POST, instance=question)

        #Validamos que los datos enviados se han correctos (campos no vacios, validaciones)
        if form.is_valid():

            #Insertamos en el base de datos el registro actualizado
            form.save()

            #retornamos a la vista question_detail y le pasamos el id
            return redirect('question_detail', question_id)

    #Si los datos no fueron enviados por post
    else:
        #Instaciamos un objeto de tipo QuestionForm y le mostramos el registro
        #capturado con el metodo get_object_or_404
        form = QuestionForm(instance=question)

    #Retornamos al template question_edit.html y le pasamos el formulario instanciado
    return render_to_response('askquestions/question_edit.html', {'form': form},
                              context_instance=RequestContext(request))

