from django.urls import path
from .views import UserLogin,LogoutView,Registerpage

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Registerpage.as_view(), name='register'),
]