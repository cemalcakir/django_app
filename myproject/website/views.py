from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.views.generic import (ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from taggit.models import Tag
from .models import Post, Comment
from .forms import CreateViewModelForm, CommentForm


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'website/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'website/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 15


class UserPostListView(ListView):
    model = Post
    template_name = 'website/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class TagView(ListView):
    model = Post
    template_name = "website/posts_by_tag.html"  # app/model_viewtype.html
    context_object_name = "posts"
    paginate_by = 15
    ordering = ["-date_posted"]

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get("tag"))


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        context['form'] = CommentForm()
        return context

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.author = self.request.user
            obj.save()
            return redirect('post-detail', post.slug)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreateViewModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = CreateViewModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        comment = self.get_object()
        return reverse('post-detail', kwargs={'slug': comment.post.slug})

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class SearchView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class UserListView(ListView):
    model = User
    template_name = 'website/user_list.html'
    context_object_name = 'users'
    paginate_by = 12

    def get_queryset(self):
        return User.objects.all().order_by("-last_login")


class TagListView(ListView):
    model = Tag
    template_name = 'website/all_tags.html'
    context_object_name = 'tags'
    paginate_by = 120

    def get_queryset(self):
        return Tag.objects.all()