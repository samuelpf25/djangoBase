from django.db import models

from stdimage.models import StdImageField

import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualizaçao', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    class Meta:
        abstract=True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )

    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

class Equipe(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations = {'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default = '#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'

    def __int__(self):
        return self.nome

class RecursosEsquerda(Base):
    ICONE_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Notebook'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Layers'),
    )

    recurso = models.CharField('Recurso Esquerda', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Recurso Esquerda'
        verbose_name_plural = 'Recursos Esquerda'

    def __str__(self):
        return self.recurso

class RecursosDireita(Base):
    ICONE_CHOICES = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Notebook'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Layers'),
    )

    recurso = models.CharField('Recurso Direita', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Recurso Direita'
        verbose_name_plural = 'Recursos Direita'

    def __str__(self):
        return self.recurso

class ContatoModel(Base):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    msg_subject = models.CharField('Assunto', max_length=100)
    message = models.TextField('Mensagem', max_length=200)
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.name

class ProdutosModel(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    unidade = models.CharField('Unidade', max_length=10)
    descricao = models.TextField('Descrição', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations = {'thumb': {'width': 120, 'height': 100, 'crop': True}})

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome