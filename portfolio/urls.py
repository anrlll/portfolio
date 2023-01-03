from django.urls import path
from .views import Prof,News,Achieve

urlpatterns = [
    path('home/',Prof.as_view()),
    path('achievement/',Achieve.as_view()),
    path('News/',News.as_view()),
]