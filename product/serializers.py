from rest_framework import serializers 
from core.models import Product

class ProductSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        