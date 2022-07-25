from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'post', PostApiView)

urlpatterns = [
    path('api/v1/update-post/<int:pk>', PostUpdateApiView.as_view(), name='post-update-api'),
    path('api/v1/create-post/', PostCreateApiView.as_view(), name='post-create-api'),
    path('api/v1/my-profile/', MyProfileApiView.as_view(), name='my-profile-api'),
    path('api/v1/posts/', PostsListAPIView.as_view(), name='posts-list-api'),
    path('', PostsListView.as_view(), name='index'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('post-create/', PostCreateView.as_view(), name='post-create'),
    path('post-edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/sing-up/', UserCreateView.as_view(), name='sing-up')
] + router.urls
