from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

@csrf_exempt
@api_view(("GET",))
def signup(request):
    return HttpResponse(status.HTTP_404_NOT_FOUND)