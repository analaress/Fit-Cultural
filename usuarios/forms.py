from django import forms

class LoginForm(forms.Form):

    cpf=forms.CharField(
        label='CPF',
        required=True,
        max_length=14,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu CPF",
            }
        ))


    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua Senha",
            }
        ),
    )

class CadastroForm(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome Completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: David Lucas Ocker",
            }
        ),
    )

    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "davidocker@gmail.com"
            }
        )
    )

    cpf=forms.CharField(
        label='CPF',
        required=True,
        max_length=14,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: 000.000.000-00",
            }
        )
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua Senha",
            }
        ),
    )

    confirma_senha = forms.CharField(
        label='Confirmar Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua Senha Novamente",
            }
        ),
    )

    def clean_confirma_senha(self):
        senha = self.cleaned_data.get('senha')
        confirma_senha = self.cleaned_data.get('confirma_senha')
        print('passou aqui')
        if senha and confirma_senha:
            if senha != confirma_senha:
                raise forms.ValidationError('As senhas digitadas não são iguais')
            else:
                return confirma_senha