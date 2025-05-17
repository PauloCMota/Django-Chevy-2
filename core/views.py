from lib2to3.fixes.fix_input import context
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import contatoform , ProdutoModelForm
from .models import Produto


# Create your views here.

def index(request):
    context = {
        'produtos' : Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    form = contatoform(request.POST or None)
    if str(request.method) == 'Post':
        if form.is_valid():
            form.send_mail()

            """
            print('mensagem enviada')
            print(f'nome: {nome}')
            print(f'e-mail: {email}')
            print(f'assunto: {assunto}')
            print(f'mensagem: {mensagem}')
            """

            messages.success(request , 'e-mail enviado com sucesso !')
            form = contatoform()

    context = {
        'form': form
    }
    return render(request, 'contato.html' , context)

def produto(request):
    #print(f'Usuario:{request.user}')
    if str(request.user)!= 'AnonymousUser':
        if str(request.method)== 'POST':
            form = ProdutoModelForm(request.POST , request.FILES)
            if form.is_valid():
                form.save()

                messages.success(request , 'Produto salvo com sucesso.')
                form = ProdutoModelForm
            else:
                messages.error(request, 'Erro ao salvar produto')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
                }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')