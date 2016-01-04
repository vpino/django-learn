from django import forms
from apis.models import PackageGeneric, PackageGenericEdu, PackageCinnamon, PackageCinnamonEdu, PackageMate, PackageMateEdu
from django.utils.translation import ugettext_lazy as _

#Hacer un formulario con Form
#class QuestionForm(forms.Form):
    #subject = forms.CharField(max_length=100, required=True)
    #description = forms.CharField(widget=forms.Textarea, required=True)

#Con ModelForm
class PackageGenericForm(forms.ModelForm):
    class Meta:
        #Le pasamos el modelo al cual le va hacer el formulario
        model = PackageGeneric
        #
        widgets={"Nombre":forms.TextInput(attrs={'placeholder':'Paquete','name':'nombre',
                                               'id':'Nombre',
                                               'class':'validate'}),
                 }
        labels = {
            'Nombre': _('Nombre del Paquete'),
        }
        #Le pasamos que campos del modelo va a crear
        fields = "__all__"

class PackageGenericEduForm(forms.ModelForm):
    class Meta:
        #Le pasamos el modelo al cual le va hacer el formulario
        model = PackageGenericEdu
        #
        widgets={"Nombre":forms.TextInput(attrs={'placeholder':'Paquete','name':'nombre',
                                               'id':'Nombre',
                                               'class':'validate'}),
                 }
        labels = {
            'Nombre': _('Nombre del Paquete'),
        }
        #Le pasamos que campos del modelo va a crear
        fields = "__all__"

class PackageCinnamonForm(forms.ModelForm):
    class Meta:
        #Le pasamos el modelo al cual le va hacer el formulario
        model = PackageCinnamon
        #
        widgets={"Nombre":forms.TextInput(attrs={'placeholder':'Paquete','name':'nombre',
                                               'id':'Nombre',
                                               'class':'validate'}),
                 }
        labels = {
            'Nombre': _('Nombre del Paquete'),
        }
        #Le pasamos que campos del modelo va a crear
        fields = "__all__"

class PackageCinnamonEduForm(forms.ModelForm):
    class Meta:
        #Le pasamos el modelo al cual le va hacer el formulario
        model = PackageCinnamonEdu
        #
        widgets={"Nombre":forms.TextInput(attrs={'placeholder':'Paquete','name':'nombre',
                                               'id':'Nombre',
                                               'class':'validate'}),
                 }
        labels = {
            'Nombre': _('Nombre del Paquete'),
        }
        #Le pasamos que campos del modelo va a crear
        fields = "__all__"

class PackageMateForm(forms.ModelForm):
    class Meta:
        #Le pasamos el modelo al cual le va hacer el formulario
        model = PackageGeneric
        #
        widgets={"Nombre":forms.TextInput(attrs={'placeholder':'Paquete','name':'nombre',
                                               'id':'Nombre',
                                               'class':'validate'}),
                 }
        labels = {
            'Nombre': _('Nombre del Paquete'),
        }
        #Le pasamos que campos del modelo va a crear
        fields = "__all__"

class PackageMateEduForm(forms.ModelForm):
    class Meta:
        #Le pasamos el modelo al cual le va hacer el formulario
        model = PackageMateEdu
        #
        widgets={"Nombre":forms.TextInput(attrs={'placeholder':'Paquete','name':'nombre',
                                               'id':'Nombre',
                                               'class':'validate'}),
                 }
        labels = {
            'Nombre': _('Nombre del Paquete'),
        }
        #Le pasamos que campos del modelo va a crear
        fields = "__all__"
