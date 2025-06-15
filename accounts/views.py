from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, MitraRegisterForm, LoginForm
from django.contrib.auth.views import LoginView

def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')  # atau bisa redirect sesuai role

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register_user.html', {'form': form})

def mitra_register(request):
    if request.user.is_authenticated:
        if request.user.role == 'mitra':
            return redirect('toko:dashboard_mitra')
        else:
            return redirect('home')

    if request.method == 'POST':
        form = MitraRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('toko:dashboard_mitra')
    else:
        form = MitraRegisterForm()
    return render(request, 'accounts/register_mitra.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'mitra':
                return redirect('toko:dashboard_mitra')
            else:
                return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.user.role == 'mitra':
            return '/toko/dashboard/'
        else:
            return '/'  # redirect ke halaman user biasa
