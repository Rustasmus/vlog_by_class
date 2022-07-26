from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .forms import *
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class UserLoginView(LoginView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            SITE_INFO
        )
        return context


class UserCreateView(CreateView):

    form_class = UserCreationForm
    template_name = 'registration/sing-up.html'
    # success_url = 'my-profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            SITE_INFO
        )
        return context

    def get_success_url(self):
        return reverse('my-profile')

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )
        login(self.request, user)
        return to_return


class MyProfileView(LoginRequiredMixin, ListView):

    model = Post
    template_name = 'vlog_app/my-profile.html'

    def get_queryset(self):
        return Post.objects.filter(
            is_draft=False,
            is_delete=False,
            user_id__id=self.request.user.id
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            SITE_INFO
        )
        return context


class PostsListView(ListView):

    model = Post
    queryset = Post.objects.filter(
        is_draft=False,
        is_delete=False
    )
    template_name = 'vlog_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            SITE_INFO
        )
        return context


class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    form_class = CreatePostForm
    template_name = 'vlog_app/post_create.html'
    # success_url = 'my-profile'

    def form_valid(self, form):
        if form.is_valid():
            form.save(
                user_id=self.request.user.id
            )
            return redirect('my-profile')
        else:
            return redirect('my-profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            SITE_INFO
        )
        return context


class PostDetailView(LoginRequiredMixin, DetailView):

    model = Post
    queryset = Post.objects.filter(
        is_draft=False,
        is_delete=False
    )
    template_name = 'vlog_app/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            SITE_INFO
        )
        return context


class PostEditView(LoginRequiredMixin, UpdateView):

    model = Post
    form_class = EditPostForm
    template_name = 'vlog_app/post-edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            SITE_INFO
        )
        return context


class PostsListAPIView(ListAPIView):

    serializer_class = PostSerializers
    queryset = Post.objects.filter(
        is_draft=False,
        is_delete=False
    )


class MyProfileApiView(ListAPIView):

    serializer_class = MyProfilePostSerializers

    def get_queryset(self):
        return Post.objects.filter(
            user_id__id=self.request.user.id,
            is_delete=False,
        )


class PostCreateApiView(CreateAPIView):

    serializer_class = CreatePostSerializers

    def perform_create(self, serializer):
        user = get_object_or_404(User, pk=self.request.user.id)
        serializer.save(user_id=user)


class PostUpdateApiView(UpdateView):

    serializer_class = PostUpdateSerializers
    queryset = Post.objects.all()


class PostApiView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetailApiView(ListAPIView):
    
    serializer_class = PostDetailSerializers
    
    queryset = Post.objects.filter(
        is_draft=False,
        is_delete=False
    )
    

