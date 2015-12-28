from django import forms
from askquestions.models import Question

#Hacer un formulario con Form
#class QuestionForm(forms.Form):
    #subject = forms.CharField(max_length=100, required=True)
    #description = forms.CharField(widget=forms.Textarea, required=True)

#Con ModelForm
class QuestionForm(forms.ModelForm):
    class Meta:
        #Le pasamos el modelo al cual le va hacer el formulario
        model = Question
        #Le pasamos que campos del modelo va a crear
        fields = "__all__"