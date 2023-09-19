from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    """
    Formulir pendaftaran pengguna baru.
    """

    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control',
        })
    )

    password1 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
            'data-toggle': 'password',
            'id': 'password',
        })
    )

    password2 = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control',
            'data-toggle': 'password',
            'id': 'password',
        })
    )

    def clean_email(self):
        """
        Validasi unik untuk alamat email.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is already taken.')
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    """
    Formulir untuk login pengguna.
    """

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        })
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        })
    )
