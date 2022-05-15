from django import forms

from .models import ContatoModel

class ContatoModelForm(forms.ModelForm):
    class Meta:
        model = ContatoModel
        fields = ['name', 'email', 'msg_subject', 'message']