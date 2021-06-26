from django.urls import path
from .views import *

urlpatterns = [
    path('tvshow/', TVShowListAPIView.as_view()),
    path('tvshow/add/', TVShowCreateAPIView.as_view()),
    path('tvshow/genre/', GenreListAPIView.as_view()),
    path('tvshow/<slug:slug>/', TVShowRetrieveAPIView.as_view()),
    path('tvshow/edit/<slug:slug>/', TVShowStateView.as_view()),
    path('release/add/', ReleaseCreateAPIView.as_view()),
    path('release/<slug:slug>/', ReleaseRetrieveAPIView.as_view()),
]
