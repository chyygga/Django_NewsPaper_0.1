from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .filters import PostFilter
from .forms import AddPostForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# from protect.views import IndexView


class NewsSearch(ListView):
    model = Post
    template_name = 'news/search.html'
    extra_context = {'title': 'Search page'}
    queryset = Post.objects.order_by('-created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsHome(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'news/home.html'
    extra_context = {'title': 'Home page'}
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-created')
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='author').exists()
        return context


class NewsDetail(LoginRequiredMixin, DetailView):
    template_name = 'news/index.html'
    queryset = Post.objects.all()


class AddPost(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'news/add.html'
    extra_context = {'title': 'Add Post'}
    success_url = reverse_lazy('home')
    permission_required = ('news.add_post',
                           )


class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = AddPostForm
    template_name = 'news/add.html'
    success_url = reverse_lazy('home')
    permission_required = ('news.change_post',
                           )

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class NewsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'news/news_delete.html'
    queryset = Post.objects.all()
    success_url = reverse_lazy('home')
    permission_required = ('news.delete_post',
                           )

class SubMe(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    success_url = reverse_lazy('index')
    permission_required = ('news.change_post',
                           )
    def sub(self, **kwargs):
        cat = Category.objects.get('category.pk')
        user = User.objects.get(user_id='user.pk')
        return cat.subscribes.add(user)


    pass
    # user = User.objects.get(pk='user.pk')
    # cat = Category.objects.get(pk='category.pk')
    # cat.subscribes.add(user)
    #
    # return redirect('/')

