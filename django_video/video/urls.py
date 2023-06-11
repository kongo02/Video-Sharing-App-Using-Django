from django.urls import path
from . import views
from . views import (
    VideoCreateView,
    video_update,
    VideoDeleteView,
    VideoListView,
    VideoDetailView,
)
urlpatterns = [
    path('', VideoListView.as_view(), name="video-list"),
    path('search', views.search, name="search"),
    path('create', VideoCreateView.as_view(), name="video-create"),
    path('video_detail/<int:pk>/', VideoDetailView.as_view(), name="video-detail"),
    path('update/<int:pk>/', views.video_update, name="video-update"),
    path('delete/<int:pk>/', VideoDeleteView.as_view(), name="video-delete"),
]
