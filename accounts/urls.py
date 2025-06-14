from django.urls import path
from .views import user_register, mitra_register, CustomLoginView
from django.contrib.auth.views import LogoutView


app_name = 'accounts'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/user/', user_register, name='register_user'),
    path('register/mitra/', mitra_register, name='register_mitra'),
]
