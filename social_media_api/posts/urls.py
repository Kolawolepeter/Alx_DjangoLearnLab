from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls

from django.urls import path
from .views import user_feed

urlpatterns = [
    path('feed/', user_feed, name='user_feed'),
]

from django.urls import path
from .views import like_post, unlike_post

urlpatterns = [
    path('posts/<int:post_id>/like/', like_post, name='like_post'),
    path('posts/<int:post_id>/unlike/', unlike_post, name='unlike_post'),
]
