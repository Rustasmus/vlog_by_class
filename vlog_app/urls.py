from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsListView.as_view(), name='index'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('post-create/', PostCreateView.as_view(), name='post-create'),
    path('post-edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/sing-up/', UserCreateView.as_view(), name='sing-up')
]