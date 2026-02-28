from django import forms
from .models import Post

INPUT_CLASS = 'w-full border border-gray-300 dark:border-gray-600 rounded-lg px-3 py-2 bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500'

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title':   forms.TextInput(attrs={'class': INPUT_CLASS}),
            'content': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 6}),
        }
