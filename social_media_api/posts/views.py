from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    user = request.user
    followed_users = user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Create notification
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb='liked your post',
        target=post
    )
    return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, post_id):
    post = Post.objects.get(id=post_id)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"detail": "Post unliked."}, status=status.HTTP_204_NO_CONTENT)
    except Like.DoesNotExist:
        return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)


# ["Post.objects.filter(author__in=following_users).order_by"]

#["generics.get_object_or_404(Post, pk=pk)"]