from django import forms


class ImageSearchForm(forms.Form):
    COLOR_CHOICES = [
        ('any', 'Всі кольори'),
        ('black_and_white', 'Чорно-біле'),
        ('black', 'Чорний'),
        ('white', 'Білий'),
        ('yellow', 'Жовтий'),
        ('orange', 'Помаранчевий'),
        ('red', 'Червоний'),
        ('purple', 'Фіолетовий'),
        ('magenta', 'Пурпуровий'),
        ('green', 'Зелений'),
        ('teal', 'Бірюзовий'),
        ('blue', 'Синій'),
    ]

    ORIENTATION_CHOICES = [
        ('any', 'Будь-яка орієнтація'),
        ('landscape', 'Горизонтальна'),
        ('portrait', 'Вертикальна'),
        ('squarish', 'Квадратна'),
    ]

    query = forms.CharField(
        label='Ключові слова',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Наприклад: minimalist web design', 'class': 'glass-input'})
    )
    color = forms.ChoiceField(
        choices=COLOR_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'glass-select'})
    )
    orientation = forms.ChoiceField(
        choices=ORIENTATION_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'glass-select'})
    )