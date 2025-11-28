from django.urls import path
from .views import BloagListCreate, BloagDetail

urlpatterns = [
    path("blog/", BloagListCreate.as_view()),
    path("blog/<int:pk>/", BloagDetail.as_view()),
]
