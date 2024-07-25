from rest_framework import serializers
from .models import Product_view
from django.contrib.auth import get_user_model   
from django.contrib.auth.models import User

User=get_user_model()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product_view
        fields=['id','Discription','Brand','Addtitle','Price','Images','Location','Phone','State','District','Year']

class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_view
        fields = '__all__'



class UserRegister(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "email", "password2"]

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        user.set_password(password)
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email') 