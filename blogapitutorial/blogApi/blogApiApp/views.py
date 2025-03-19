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
def GetAllPosts(request):
    get_posts = Post.objects.all()
    serializer = PostSerializer(get_posts, many=True) # get_posts includes multiple items. So mention that parameter many=True
    
    return Response(serializer.data)

@api_view(['GET','POST'])
def CreatePost(request):
    data = request.data
    serializer = PostSerializer(data = data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({'Success':'The post was successfully Created'},status=201)
    else:
        return Response(serializer.errors,status=400)