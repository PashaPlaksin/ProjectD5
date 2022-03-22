from django.forms import ModelForm
from .models import Post, User


# Создаём модельную форму
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'post_types', 'categories', 'title_post', 'post_text']


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = '__all__'