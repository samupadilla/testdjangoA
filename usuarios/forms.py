from django import forms
from . models import Aprendiz

class FormularioAprendiz(forms.ModelForm):
    class Meta:
        model=Aprendiz
        fields='__all__'
        # fields = ["name", "photo", "sureName", "documento", "genero","ficha"]
        # print('--------',fields)
        #widgets={'fecha_nacimiento':forms.DateInput(attrs={'type':'date'})}

    # def clean(self):
    #     print (self.cleaned_data)
    #     return self.cleaned_data

    # def __init__(self, *args, **kwargs):
    #     super(FormularioAprendiz, self).__init__(*args, **kwargs)
    #     self.fields['photo'].required = False