from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget
class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model=Article
        fields='__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write the Title here .. '}),
            # 'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write the Content here .. '}),
            'source': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write the Source here .. '}),
            'image': forms.FileInput(attrs={'class':'custom-file-input','id':'inputGroupFile01','aria-describedby':'inputGroupFileAddon01'}),

            
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['message']
        widgets = {
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'What are you thinking...', 'id':'message', 'rows':'3'}),
        }
