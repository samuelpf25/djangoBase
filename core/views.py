from django.contrib import messages

from django.views.generic import TemplateView, FormView

from .models import Servico, Equipe, RecursosEsquerda, RecursosDireita, ProdutosModel

from .forms import ContatoModelForm

from django.shortcuts import render

class SuccessMessageMixin:
    """
    Add a success message on successful form submission.
    """
    success_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

class IndexView(SuccessMessageMixin, TemplateView):
    template_name = 'index.html'
    success_message = ''
    def get_context_data(self, **kwargs):

        print('passou por aqui GET!')
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['equipes'] = Equipe.objects.all()
        context['recursosesquerda'] = RecursosEsquerda.objects.all()
        context['recursosdireita'] = RecursosDireita.objects.all()
        context['produtos'] = ProdutosModel.objects.all()
        context['form'] = ContatoModelForm()
        return context

    def post(self, request, *args, **kwargs):
        print('Abriu formulário')
        if str(request.method) == 'POST':
            print('Método POST')
            form = ContatoModelForm(request.POST, request.FILES)
            # print(form)
            if form.is_valid():
                # prod = form.save()
                # print(f'Nome: {prod.nome}')
                # print(f'Preço: {prod.preco}')
                # print(f'Estoque: {prod.estoque}')
                # print(f'Imagem: {prod.imagem}')

                form.save()  # salvando dados

                print('Formulário Salvo')
                messages.success(request, 'Contato registrado com sucesso!')

                form = ContatoModelForm()  # zerando os campos do formulário
            else:
                messages.error(request, 'Erro ao salvar produto!')
        else:
            form = ContatoModelForm()

        context = {'form': form}
        return render(request, 'index.html', context)



# def IndexFormView(request):
#     #if str(request.user) != 'AnonymousUser':
#     print('Abriu formulário')
#     if str(request.method) == 'POST':
#         print('Método POST')
#         form = ContatoModelForm(request.POST, request.FILES)
#         #print(form)
#         if form.is_valid():
#             # prod = form.save()
#             # print(f'Nome: {prod.nome}')
#             # print(f'Preço: {prod.preco}')
#             # print(f'Estoque: {prod.estoque}')
#             # print(f'Imagem: {prod.imagem}')
#
#             form.save() #salvando dados
#
#             print('Formulário Salvo')
#             messages.success(request, 'Produto salvo com sucesso!')
#
#
#             form = ContatoModelForm() #zerando os campos do formulário
#         else:
#             messages.error(request,'Erro ao salvar produto!')
#     else:
#         form = ContatoModelForm()
#
#     context = {'form': form}
#     return render(request,'index.html',context)
