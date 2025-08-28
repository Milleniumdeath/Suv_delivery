from django.db.models import Q
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.openapi import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import *
from .serializers import *

class SuvAPIView(APIView):
    def get(self, request):
        suvlar = Suv.objects.all()
        serializer = SuvSerializer(suvlar, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = SuvSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "success": True,
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "success": False,
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        suv = get_object_or_404(Suv, pk=pk)
        suv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def validate_litr(self, value):
        if value.litr >= 19:
            raise serializers.ValidationError(
                "Bunday katta litrlarda suv sotilmaydi!"
            )
        return value

class MijozAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                description='Search by name or context.',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING
            ),
        ]
    )
    def get(self, request):
        mijozlar = Mijoz.objects.all()
        search = request.GET.get('search')
        if search:
            mijozlar = mijozlar.filter(Q(ism__icontains=search) | Q(tel_raqam__icontains=search))




        serializer = MijozSerializer(mijozlar, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = MijozSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "success": True,
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "success": False,
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        mijoz = get_object_or_404(Mijoz, pk=pk)
        mijoz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HaydovchiListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Haydovchi.objects.all()
    serializer_class = HaydovchiSerializer

    def get_object(self):
        return self.request.user

class HaydovchiRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Haydovchi.objects.all()
    serializer_class = HaydovchiDetailsSerializer

    def get_object(self):
        return self.request.user

class BuyurtmaListCreateAPIView(ListCreateAPIView):
    permission_classes = [ IsAuthenticated]
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def validate_mijoz(self, value):
        if value.mijoz.qarz >= 500000:
            raise serializers.ValidationError(
                "Qarzingiz juda ko’p, buyurtma qilolmaysiz!"
            )
        return value

