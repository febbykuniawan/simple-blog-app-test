from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import UserProfile
from .forms import ProfileForm

class UserProfileView(LoginRequiredMixin, View):
    """
    Tampilan untuk menampilkan profil pengguna.
    """

    template_name = 'profile.html'

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(UserProfile, user=user)

        article_count = user.article_set.count()
        following_count = user.user_profile.followers.count()

        context = {
            'user': user,
            'profile': profile,
            'article_count': article_count,
            'following_count': following_count
        }

        return render(request, self.template_name, context)
    
    def post(self, request, username):
        user_to_follow = get_object_or_404(User, username=username)

        if request.user != user_to_follow:
            profile_user = UserProfile.objects.get(user=user_to_follow)

            if request.user not in profile_user.followers.all():
                profile_user.followers.add(request.user)
                messages.success(request, f'You are now following {user_to_follow.username}.')
            else:
                profile_user.followers.remove(request.user)
                messages.success(request, f'You have unfollowed {user_to_follow.username}.')

        return redirect('user-profile', username=user_to_follow.username)

class EditProfileView(LoginRequiredMixin, UpdateView):
    """
    Tampilan untuk mengedit profil pengguna.
    """

    model = UserProfile
    form_class = ProfileForm
    template_name = 'editProfile.html'
    success_url = reverse_lazy('user-profile')

    def get_object(self, queryset=None):
        return self.request.user.user_profile

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid form submission. Please check the entered data.')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse('user-profile', kwargs={'username': self.request.user.username})
