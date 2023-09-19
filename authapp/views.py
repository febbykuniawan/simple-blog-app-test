from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authapp.forms import SignUpForm, LoginForm
from userprofileapp.models import UserProfile

class Register(generic.CreateView):
    """
    Tampilan untuk registrasi pengguna baru.
    """

    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        
        UserProfile.objects.create(user=self.object)
        
        messages.success(self.request, 'Registration successful. You can now log in.')
        return response

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class Login(generic.FormView):
    """
    Tampilan untuk login pengguna.
    """

    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            messages.success(self.request, 'Login successful.')
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password.')
            return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class LogoutView(generic.View):
    """
    Tampilan untuk logout pengguna.
    """

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect(reverse_lazy('home'))
