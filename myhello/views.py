#from django.shortcuts import render
# Create your views here.
 #from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import Post
from django.core.serializers.json import DjangoJSONEncoder
@api_view(['GET'])
def add_post(request):
    title=request.GET.get('title','')
    content=request.GET.get('content','')
    photo=request.GET.get('photo','')
    location=request.GET.get('location','')

    new_post=Post()
    new_post.title=title
    new_post.content=content
    new_post.photo=photo
    new_post.location=location
    new_post.save()
    if title:
      return Response({"data": title +"insert!"},status=status.HTTP_200_OK)
    else:
      return Response({
        "res":"parameter:name is None"},
        status=status.HTTP_400_BAD_REQUEST

      )
@api_view(['GET'])

def list_post(request):
  posts=Post.objects.all().values()
  return JsonResponse(list(posts),safe=False)
  # return Response({
  #   "data":json.dumps(list(posts),sort_keys=True,indent=1,cls=DjangoJSONEncoder)},
  #   status=status.HTTP_200_OK)