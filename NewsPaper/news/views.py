from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
from .models import Post, User
from .filters import PostFilter
from .forms import PostForm, UserForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class PostSearch(ListView):
    model = Post
    template_name = 'news/search.html'
    context_object_name = 'posts_search'
    ordering = ['-time_add_post']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostCreate(CreateView):
    template_name = 'news/news_create.html'
    form_class = PostForm


class PostList(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts'
    ordering = ['-time_add_post']
    paginate_by = 10


class PostDetail(DetailView):
    model = Post  #
    template_name = 'news/news_text.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    template_name = 'news/news_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'news/news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


#class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#    template_name = 'news/author_update.html'
#    form_class = UserForm
#    success_url = '/'

    #def get_object(self, **kwargs):
     #   id = self.kwargs.get('pk')
      #  return User.objects.get(pk=id)


class AddNews(PermissionRequiredMixin, PostCreate):
    permission_required = ('news.add_post',)


class ChangeNews(PermissionRequiredMixin, PostUpdateView):
    permission_required = ('news.change_post',)


class DeleteNews(PermissionRequiredMixin, PostDeleteView):
    permission_required = ('news.delete_post', )


#class ViewNews(PermissionRequiredMixin, PostList):
#    permission_required = ('news.view_post', )

