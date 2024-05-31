from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user_app.api.views import RegisterationView, LogoutView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', RegisterationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='register'),
]
