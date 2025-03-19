from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostSerializertwo(ModelSerializer):
    class Meta:
        model = Post
        fields = ['content']   # Serialize only the content field