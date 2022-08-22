from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drfapp.serializers import StudentSerializers
from drfapp.models import Student
from django.http import JsonResponse


class TesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *arg, **kwargs):
        qs = Student.objects.all()
        serializer = StudentSerializers(qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *arg, **kwargs):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
