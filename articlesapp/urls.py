from django.urls import path
from . import views

urlpatterns = [
    path('my-article/', views.MyArticleView.as_view(), name='my-article'),
    path('create-article/', views.CreateArticleView.as_view(), name='create-article'),
    path('show-article/<int:pk>/', views.ShowArticleView.as_view(), name='show-article'),
    path('edit-article/<int:pk>/', views.EditArticleView.as_view(), name='edit-article'),
]
