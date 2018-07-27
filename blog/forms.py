from django import forms
from .models import publication, Comments

class PostForm(forms.ModelForm):

    title = forms.CharField(label='Название блога',
                            max_length=30,
                            min_length= 2,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    short_description = forms.CharField(label='Краткое описание',
                                        max_length=30,
                                        min_length= 10,
                                        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = publication
        fields = ('title', 'short_description', 'text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '10', 'cols': '20'})
        }

class CommentForm(forms.ModelForm):
    """Форма комментариев к статьям
    """
    class Meta:
        model = Comments
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': '2', 'cols': '2'})
        }