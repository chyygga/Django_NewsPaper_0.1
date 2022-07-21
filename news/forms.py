from django import forms
from .models import *


class AddPostForm(forms.ModelForm):

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['author'] = self.request.user.username
    #     return context

    class Meta:
        model = Post
        fields = ('author', 'post_type', 'title', 'cats', 'text'
                  )
