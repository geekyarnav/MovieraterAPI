from rest_framework import serializers
from .models import Movie, Rating
# from django.contrib.auth.models import User

# from rest_framework.authtoken.models import Token
# RESTRICTION IN APPLICATION


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id','movie','user','stars')

class MovieSerializer(serializers.ModelSerializer):
    Rating=RatingSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id','title','description','Rating')



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id','username', 'password')
#         extra_Kwargs = {'password': {'write_only': True,
#         'required': True}}
    
#     # def create(self, validated_data):
#     #     user = User.objects.create_user(**validated_data)
#     #     Token.objects.create(user=user)
#     #     return user