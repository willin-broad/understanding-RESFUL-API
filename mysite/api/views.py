from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView

# Create your views here.
#views the table ..create path
class BlogPostlistCreate(generics.ListCreateAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer

    def delete(self , request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#here one can udate..delete records
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    lookup_field="pk"

class BlogPostList(APIView):
    def get(self, request, format=None) :
        # get title fromquery parameters(empty string default)
        title =request.query_params.get("title","")
        
        if title:
            #filtering queryset based on tittle
            blog_posts=BlogPost.objects,filter(title_icontains=title)
        else:
            #return all posts if no query title is provided
            blog_posts=BlogPost.objects.all()
        serializer=BlogPostSerializer(blog_posts,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)