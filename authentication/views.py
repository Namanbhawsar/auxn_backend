from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import SignupSerializer


class SignupView(APIView):

    @swagger_auto_schema(
        request_body=SignupSerializer,
        operation_description="User Signup API",
        responses={201: "User created successfully", 400: "Bad request"},
    )
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)