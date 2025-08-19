from .models import Card
from django.forms import ModelForm, TextInput, Textarea

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['word', 'definition']

        widgets = {
            "word": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Слово'
            }),
            "definition": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Определение',
                'rows': 1,
            }),
        }