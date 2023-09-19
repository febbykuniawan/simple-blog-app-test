from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    """
    Formulir untuk mengedit profil pengguna.
    """

    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']

        widgets = {
            'bio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Profile Bio'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Profile'
            })
        }
