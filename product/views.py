from rest_framework.viewsets import ModelViewSet
from core.models import Product
from .serializers import ProductSeralizer
from rest_framework.permissions import AllowAny,IsAuthenticated

class ProductView(ModelViewSet):
    permission_classes=[AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    
    def get_permissions(self):
        if self.action == 'destroy':
            return [IsAuthenticated()]
        else:
            return[AllowAny()]
