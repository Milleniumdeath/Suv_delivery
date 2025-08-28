from django.urls import path, include
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
from users.views import *

#JWT Urls
urlpatterns = [
    path('token/', token_obtain_pair , name='token_obtain_pair'),
    path('token/refresh/', token_refresh , name='token_refresh'),
    path('auth/', include('users.urls')),
    path('', include('main.urls')),

]

#USER Urls
urlpatterns += [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('admin/', UserRetrieveAPIView.as_view(), name='retrieve'),

]