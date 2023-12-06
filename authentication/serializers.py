from django.contrib.auth import get_user_model
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields = ("name","email","password","phone","address")
    
    def save(self):
        user=get_user_model()(
            name=self.validated_data["name"],
            email=self.validated_data["email"],
            phone=self.validated_data["phone"],
            address=self.validated_data["address"]
        )
        password = self.validated_data["password"]

        user.set_password(password)
        user.save()

        return user
    
    
# class LoginSerializer(serializers.Serializer):
#     email=serializers.EmailField()
#     password=serializers.CharField()