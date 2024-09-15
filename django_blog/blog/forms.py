from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

from django import forms
from .models import Post
from taggit.forms import TagWidget  # Import TagWidget for tag field

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags' in the fields list
        widgets = {
            'tags': TagWidget(),  # Use TagWidget for the tags field
        }
