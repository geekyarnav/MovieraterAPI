from django.shortcuts import render
from .models import Movie,Rating
from .serializers import MovieSerializer
from .serializers import RatingSerializer
# from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework.decorators import action
from django.contrib.auth.models import User
# --------------authentication-----------
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated,AllowAny

        
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (AllowAny,)
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        
        if 'stars' in request.data:
            
            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user
            
            try :
                rating = Rating.objects.get(user= user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many= False)
                response = {"message": 'Rating updated', 'result':serializer.data }
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user= user, movie=movie)
                serializer - RatingSerializer(rating, many=False)
                response = {"message":'Rating created','result':serializer.data}
        
        else:
            response = {"message": "You need to provide stars"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST) 
    def create(self, request, *args, **kwargs):
        movie_data=request.data
        movie=Movie.objects.create()  
        movie.save()  
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
 

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

     
