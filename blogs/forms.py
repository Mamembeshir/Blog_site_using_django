from django import forms
from .models import Post, Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('author','title','text','image')

        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium_editor_textarea'})
        }
class CommentsForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('author','text')
        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
class UserCreationForm(AuthUserCreationForm):
    email=forms.EmailField(max_length=254)
    bio=forms.CharField(max_length=500)
    profile_pic=forms.ImageField(required=False)

    class Meta:
        model=User
        fields = ('username', 'email', 'password1','password2','bio', 'profile_pic')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].help_text=None