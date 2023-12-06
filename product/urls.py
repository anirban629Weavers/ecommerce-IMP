from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import ProductView

urlpatterns = []

router=routers.SimpleRouter()
router.register('product',ProductView)
urlpatterns += router.urls

