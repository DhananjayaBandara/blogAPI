from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    return Response({'Success':'The setup was successful'})

@api_view(['GET'])
def getAllPosts(request):
    get_posts = Post.objects.all()
    serializer = PostSerializer(get_posts)
    
    return Response(serializer.data)
