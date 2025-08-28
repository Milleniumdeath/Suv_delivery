from django.urls import path
from .views import *

urlpatterns = [
    path('buyurtma/', BuyurtmaListCreateAPIView.as_view(),),
    path('haydovchilar/', HaydovchiListAPIView.as_view(), name='haydovchi-list'),
    path('haydovchi/', HaydovchiDetailsSerializer.as_view(), name='haydovchi-retrieve'),
    path('suvlar/', SuvAPIView.as_view(), name='suv'),



]