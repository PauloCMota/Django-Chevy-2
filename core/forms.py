from django import forms
from django.core.mail import EmailMessage

from core.models import Produto


class contatoform(forms.Form):
    nome = forms.CharField(label='nome', max_length=100)
    email = forms.EmailField(label='e-mail', max_length=100)
    assunto = forms.CharField(label='assunto', max_length=120)
    mensagem = forms.CharField(label='mensagem' , widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'nome:{nome}\n e-mail:{email} \n assunto: {assunto} \n mensagem: {mensagem}'

        mail = EmailMessage(
            subject='e-mail enviado pelo sistem django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br'],
            headers={'replay-to': email}
        )

        mail.send()

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']


