from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),  # Make sure you have a profile view
]

from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]

from django.urls import path
from .views import (
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    # Other URL patterns for blog posts, etc.

    # URL for creating a new comment on a post
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),

    # URL for updating an existing comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),

    # URL for deleting an existing comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]

from django.urls import path
from .views import post_search, PostsByTagView

urlpatterns = [
    # Other URLs for the blog
    path('search/', post_search, name='post_search'),
    path('tags/<slug:tag_slug>/', PostsByTagView.as_view(), name='posts_by_tag'),
]

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostByTagListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('tags/<slug:slug>/', PostByTagListView.as_view(), name='post-by-tag'),
]
