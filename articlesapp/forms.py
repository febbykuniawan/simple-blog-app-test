from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    """
    Formulir untuk membuat atau mengedit artikel.
    """

    class Meta:
        model = Article
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title article'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Content article',
                'style': 'height: 200px'
            }),
        }
