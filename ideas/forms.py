from django import forms
from .models import Idea


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'tags']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


IDEA_TYPE_CHOICES = [
    ("general", "Загальна"),
    ("header", "Header"),
    ("footer", "Footer"),
    ("landing", "Landing Page"),
    ("portfolio", "Portfolio"),
    ("pet-project", "Pet-project"),
]

class IdeaGenerationForm(forms.Form):
    keywords = forms.CharField(
        label="Ключові слова",
        help_text="Введіть кілька слів через кому"
    )
    mood = forms.ChoiceField(
        choices=[
            ("dark", "Темна атмосфера"),
            ("bright", "Світла"),
            ("mystery", "Містика"),
            ("sci-fi", "Наукова фантастика"),
            ("romance", "Романтика"),
        ],
        label="Настрій",
        required=False
    )
    idea_type = forms.ChoiceField(
        choices=IDEA_TYPE_CHOICES,
        label="Тип ідеї",
        required=False
    )


