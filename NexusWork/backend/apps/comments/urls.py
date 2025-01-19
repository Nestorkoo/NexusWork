from django.urls import path,include

from backend.apps.comments.views import CommentViewDetail, CommentCreate, CommentDelete

urlpatterns = [
    path('comments/team/<int:pk>/', CommentViewDetail.as_view(), name='current_comment_detail'),
    path('comment/create/', CommentCreate.as_view(), name='comment_create'),
    path('comment/delete/<int:pk>/', CommentDelete.as_view(), name='comment_delete'),
]