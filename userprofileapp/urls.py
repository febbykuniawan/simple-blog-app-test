from django.urls import path
from . import views

urlpatterns = [
    path('user-profile/<str:username>/', views.UserProfileView.as_view(), name='user-profile'),
    path('edit-profile/', views.EditProfileView.as_view(), name='edit-profile'),
]