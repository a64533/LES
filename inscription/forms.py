from django import forms

from .models import *

class InscriptionForm(forms.Form):
#    nome = forms.CharField(label="Escreva o seu nome:")
#    idade = forms.IntegerField(label="Insira a sua idade:")

    def __init__(self, event_type_id, form_type_id, *args, **kwargs):
        super(InscriptionForm, self).__init__(*args, **kwargs)
        form = Formulario.objects.get(tipo_de_eventosid = event_type_id, tipo_de_formularioid = form_type_id)
        #FormularioPerguntasDoFormulario_model = FormularioPerguntasDoFormulario.objects.filter(formularioid = form.id)
        #questions = PerguntasDoFormulario.objects.filter(id = FormularioPerguntasDoFormulario.objects.filter(formularioid = form.id))
        #questions = form.formularioperguntasdoformulario_set.all()
        questions = PerguntasDoFormulario.objects.all()

        for question in questions:
            if question.tipo_de_perguntaid_id == 1: #desenvolvimento
                self.fields[str(question.id)] = forms.CharField(label=question.label)
            elif question.tipo_de_perguntaid_id == 2: #escolha multipla
                 self.fields[str(question.id)] = forms.ModelChoiceField(label=question.label, queryset=OpcoesDoTipoDePergunta.objects.filter(perguntas_do_formularioid=question.id))
            elif question.tipo_de_perguntaid_id == 3: #checkbox
                self.fields[str(question.id)] = forms.BooleanField(label=question.label)  