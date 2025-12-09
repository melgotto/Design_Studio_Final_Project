from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'Тема обговорення'}),
            'content': forms.Textarea(attrs={'class': 'glass-input', 'rows': 5, 'placeholder': 'Опишіть вашу ідею...'}),
            'tags': forms.TextInput(attrs={'class': 'glass-input', 'placeholder': 'теги через кому'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'glass-input', 'rows': 3, 'placeholder': 'Напишіть коментар...'}),
        }