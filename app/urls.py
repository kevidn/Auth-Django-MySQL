from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'),
]