urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
]

#["login/"]

from django.urls import path
from .views import follow_user, unfollow_user

urlpatterns = [
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]
