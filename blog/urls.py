from django.urls import path
from . import views
from .views import (
    CreationListView,
    CreationDetailView,
    CreationCreateView,
    CreationUpdateView,
    CreationDeleteView,
    LikeView
)

app_name = 'blog'

urlpatterns = [
    path('', CreationListView.as_view(template_name='blog/creation-blog.html'), name='main'),
    path('blog/<int:pk>/', CreationDetailView.as_view(), name='detail'),
    path('blog/new/', CreationCreateView.as_view(), name='create'),
    path('blog/<int:pk>/update/', CreationUpdateView.as_view(), name='update'),
    path('blog/<int:pk>/delete/', CreationDeleteView.as_view(), name='delete'),
    path('like/<int:pk>', LikeView, name='like_creation'),
]
