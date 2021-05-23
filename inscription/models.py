# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.
    gabinete = models.CharField(db_column='Gabinete', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrador'


class Disponibilidade(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    espacoid = models.ForeignKey('Espaco', models.DO_NOTHING, db_column='EspacoID')  # Field name made lowercase.
    servicoid = models.ForeignKey('Servico', models.DO_NOTHING, db_column='ServicoID')  # Field name made lowercase.
    equipamentoid = models.ForeignKey('Equipamento', models.DO_NOTHING, db_column='EquipamentoID')  # Field name made lowercase.
    disponibilidade = models.TextField(db_column='Disponibilidade')  # Field name made lowercase. This field type is a guess.
    datareserva = models.DateTimeField(db_column='DataReserva')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'disponibilidade'


class Equipamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fornecedorid = models.ForeignKey('Fornecedor', models.DO_NOTHING, db_column='FornecedorID')  # Field name made lowercase.
    proponenteutilizadorid = models.IntegerField(db_column='ProponenteUtilizadorID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipamento'


class EquipamentoEvento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    equipamentoid = models.ForeignKey(Equipamento, models.DO_NOTHING, db_column='EquipamentoID')  # Field name made lowercase.
    eventoid = models.ForeignKey('Evento', models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade')  # Field name made lowercase.
    datainicial = models.DateTimeField(db_column='DataInicial')  # Field name made lowercase.
    datafinal = models.DateTimeField(db_column='DataFinal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipamento_evento'


class Espaco(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=255)  # Field name made lowercase.
    capacidade = models.IntegerField(db_column='Capacidade')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'espaco'


class EspacoEvento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    espacoid = models.ForeignKey(Espaco, models.DO_NOTHING, db_column='EspacoID')  # Field name made lowercase.
    eventoid = models.ForeignKey('Evento', models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade')  # Field name made lowercase.
    datainicial = models.DateTimeField(db_column='DataInicial')  # Field name made lowercase.
    datafinal = models.DateTimeField(db_column='DataFinal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'espaco_evento'


class Evento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo_de_eventosid = models.ForeignKey('TipoDeEventos', models.DO_NOTHING, db_column='Tipo de EventosID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    formularioidinscricao = models.ForeignKey('Formulario', related_name='formularioinscricao', on_delete=models.CASCADE, db_column='FormularioIDInscricao', blank=True, null=True)  # Field name made lowercase.
    formularioidfeedback = models.ForeignKey('Formulario', related_name='formulariofeedback', on_delete=models.CASCADE, db_column='FormularioIDFeedback', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.
    datainicio = models.DateTimeField(db_column='DataInicio')  # Field name made lowercase.
    datafinal = models.DateTimeField(db_column='DataFinal')  # Field name made lowercase.
    numeroparticipantes = models.IntegerField(db_column='NumeroParticipantes')  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evento'


class Feedback(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    inscricaoid = models.ForeignKey('Inscricao', models.DO_NOTHING, db_column='InscricaoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feedback'


class Formulario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID')  # Field name made lowercase.
    tipo_de_eventosid = models.ForeignKey('TipoDeEventos', models.DO_NOTHING, db_column='Tipo de EventosID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tipo_de_formularioid = models.ForeignKey('TipoDeFormulario', models.DO_NOTHING, db_column='Tipo de FormularioID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    certificadosparticipacao = models.TextField(db_column='CertificadosParticipacao')  # Field name made lowercase. This field type is a guess.
    servicos = models.TextField(db_column='Servicos')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'formulario'


class FormularioPerguntasDoFormulario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    formularioid = models.ForeignKey(Formulario, models.DO_NOTHING, db_column='FormularioID')  # Field name made lowercase.
    perguntas_do_formularioid = models.ForeignKey('PerguntasDoFormulario', models.DO_NOTHING, db_column='Perguntas do formularioID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'formulario_perguntas do formulario'
        unique_together = ('formularioid', 'perguntas_do_formularioid',)


class Fornecedor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fornecedor'


class Inscricao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    participanteutilizadorid = models.ForeignKey('Participante', models.DO_NOTHING, db_column='ParticipanteUtilizadorID')  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inscricao'


class Notificacao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.
    criadoem = models.CharField(db_column='CriadoEm', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notificacao'


class NotificaoUtilizador(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    notificacaoid = models.OneToOneField(Notificacao, models.DO_NOTHING, db_column='NotificacaoID')  # Field name made lowercase.
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notificao_utilizador'


class OpcoesDoTipoDePergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    perguntas_do_formularioid = models.ForeignKey('PerguntasDoFormulario', models.DO_NOTHING, db_column='Perguntas do formularioID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    opcoes_de_pergunta = models.CharField(db_column='opcoes de pergunta', max_length=255)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'opcoes do tipo de pergunta'


class Participante(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participante'


class Pedido(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo_de_recursoid = models.ForeignKey('TipoDeRecurso', models.DO_NOTHING, db_column='Tipo de recursoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eventoid = models.ForeignKey(Evento, models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255)  # Field name made lowercase.
    limite = models.IntegerField(db_column='Limite')  # Field name made lowercase.
    quantidade = models.IntegerField(db_column='Quantidade')  # Field name made lowercase.
    datainicial = models.DateTimeField(db_column='DataInicial')  # Field name made lowercase.
    datafinal = models.DateTimeField(db_column='DataFinal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedido'


class PerguntasDoFormulario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo_de_perguntaid = models.ForeignKey('TipoDePergunta', models.DO_NOTHING, db_column='Tipo de PerguntaID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    label = models.CharField(db_column='Label', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'perguntas do formulario'


class Proponente(models.Model):
    utilizadorid = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='UtilizadorID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proponente'


class ProponenteEquipamento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    proponenteutilizadorid = models.ForeignKey(Proponente, models.DO_NOTHING, db_column='ProponenteUtilizadorID')  # Field name made lowercase.
    equipamentoid = models.ForeignKey(Equipamento, models.DO_NOTHING, db_column='EquipamentoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proponente_equipamento'


class ProponenteServico(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    proponenteutilizadorid = models.OneToOneField(Proponente, models.DO_NOTHING, db_column='ProponenteUtilizadorID')  # Field name made lowercase.
    servicoid = models.OneToOneField('Servico', models.DO_NOTHING, db_column='ServicoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proponente_servico'


class RespostaDoFormulario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    perguntas_do_formularioid = models.ForeignKey(PerguntasDoFormulario, models.DO_NOTHING, db_column='Perguntas do formularioID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eventoid = models.ForeignKey(Evento, models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.
    opcoes_do_tipo_de_perguntaid = models.ForeignKey(OpcoesDoTipoDePergunta, models.DO_NOTHING, db_column='Opcoes do tipo de perguntaID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    feedbackid = models.ForeignKey(Feedback, models.DO_NOTHING, db_column='FeedbackID')  # Field name made lowercase.
    inscricaoid = models.ForeignKey(Inscricao, models.DO_NOTHING, db_column='InscricaoID')  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resposta do formulario'


class Servico(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo_de_servicoid = models.ForeignKey('TipoDeServico', models.DO_NOTHING, db_column='Tipo de ServicoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fornecedorid = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='FornecedorID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servico'


class ServicoEvento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    eventoid = models.ForeignKey(Evento, models.DO_NOTHING, db_column='EventoID')  # Field name made lowercase.
    servicoid = models.ForeignKey(Servico, models.DO_NOTHING, db_column='ServicoID')  # Field name made lowercase.
    datainicial = models.DateTimeField(db_column='DataInicial')  # Field name made lowercase.
    datafinal = models.DateTimeField(db_column='DataFinal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servico_evento'


class TipoDeEventos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo de eventos'


class TipoDeFormulario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo de formulario'


class TipoDePergunta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo de pergunta'


class TipoDeRecurso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo de recurso'


class TipoDeServico(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo de servico'


class Utilizador(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=255)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilizador'
