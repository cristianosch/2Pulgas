from django import forms
from django.forms import ModelForm
from .models import Comment, Reply


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        labels = {"text":"Add your comment:"}

        widgets = {            
            'text': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':10, 'placeholder':"Enter Your Comment"}),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_text',)
        
        labels = {"reply_text":"Reply Comment:"}

        widgets = {            
            'reply_text': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':10, 'placeholder':"Reply Comment"}),
        }