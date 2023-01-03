from django.shortcuts import render
from .models import Profile,Achievement,News
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
# Create your views here.

class Prof(TemplateView):
    template_name = "index.html"
    model = Profile

class Achieve(ListView):
    template_name = "achievement.html"
    model = Achievement

class News(ListView):
    template_name = "news.html"
    model = News
