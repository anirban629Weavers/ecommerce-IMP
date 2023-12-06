from django.urls import path
from .views import RegisterAPI,LoginAPI

urlpatterns = [
    path("register/",RegisterAPI.as_view(),name="register-view"),
    path("login/",LoginAPI.as_view(),name="login-view")
]
