from django.conf.urls import url
from .views import authenticate_user, CreateUserAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    url('create/', CreateUserAPIView.as_view()),
    url('update/', UserRetrieveUpdateAPIView.as_view()),
    url('obtain_token/', authenticate_user),


]
