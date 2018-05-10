from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import permissions

from posts.models import Posts
from posts.serializers import PostSerializer


class PostsList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request):
        if request.user.is_authenticated():
            posts = Posts.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        return Response({"error": "sem autorização"})

    def post(self, request):
        if request.user.is_authenticated():
            data = JSONParser().parse(request)
            serializer = PostSerializer(data=data)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "sem autorização"})

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
