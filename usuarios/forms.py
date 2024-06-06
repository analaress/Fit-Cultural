from django import forms
from django.core.validators import RegexValidator

class LoginForm(forms.Form):
    cpf=forms.CharField(
        label='CPF',
        required=True,
        max_length=14,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: 000.000.000-00",
            }
        ),
        validators=[
            RegexValidator(
                regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
                message='O CPF deve estar no formato 000.000.000-00',
            ),
        ],
    )

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