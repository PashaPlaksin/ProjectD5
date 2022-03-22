from django_filters import FilterSet, DateTimeFromToRangeFilter, CharFilter
from django_filters.widgets import RangeWidget
from .models import Post
from datetime import datetime


class PostFilter(FilterSet):

    time_add_post = DateTimeFromToRangeFilter (lookup_expr=('icontains'), widget=RangeWidget(attrs={'type':'datetime-local'}),label='Дата публикации')
    title_post = CharFilter (lookup_expr='icontains',label='Заголовок')

    class Meta:
        model = Post
        fields = ['author','time_add_post', 'title_post']


