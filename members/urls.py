
from django.urls import path
from .views import UserRegisterView
# pk is used to index the post
urlpatterns = [
    path('registration/', UserRegisterView.as_view(), name='register'),
]
