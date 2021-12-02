from django import forms

from sistema.models import Arquivo, Documento, Caçifo, Secção

class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class SecçãoForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Secção
        exclude = ('usuario','modificador')

class CaçifoForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Caçifo
        exclude = ('usuario','modificador')

class ArquivoForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Arquivo
        exclude = ('usuario','modificador')

class DocumentoForm(BaseForm, forms.ModelForm):
    class Meta:
        model = Documento
        exclude = ('usuario','modificador')