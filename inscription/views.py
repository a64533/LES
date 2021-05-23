from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Evento, RespostaDoFormulario, PerguntasDoFormulario, Inscricao
from .forms import InscriptionForm

user_test_id = 1

def all_events(request):
    events = Evento.objects.all()
    return render(request, 'inscription/all_events.html', {'events': events})

def event_page(request, event_id):
    evento = get_object_or_404(Evento, id=event_id)
    return render(request, 'inscription/event_page.html', {'event': evento})

def inscription_action(request, event_id):
    event = get_object_or_404(Evento, id=event_id)
    form_type_id = 1
    if request.method == 'POST':
        form = InscriptionForm(request.POST, event.tipo_de_eventosid, form_type_id)
        if form.is_valid():
            for question, answer in form.cleaned_data.items():
                RespostaDoFormulario_model = RespostaDoFormulario(perguntas_do_formularioid=PerguntasDoFormulario.objects.get(id=1), eventoid=Evento.objects.get(id=event_id), resposta=answer)
                RespostaDoFormulario_model.save()
        else:
            return render(request, "inscription/inscription_form.html", {'form': InscriptionForm, 'event_id': event_id})

    else:
        return render(request, "inscription/inscription_form.html", {'form': InscriptionForm, 'event_id': event_id})

    message = "Inscription successful"
    return render(request, 'inscription/message.html', {'MESSAGE': message})

def inscription_form(request, event_id):
    event = get_object_or_404(Evento, id=event_id)
    form_type_id = 1
    return render(request, "inscription/inscription_form.html", {'form': InscriptionForm(event.tipo_de_eventosid, form_type_id), 'event_id': event_id})