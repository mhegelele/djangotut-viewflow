"""
    polls URL Configuration
"""
from django.urls import include, path
from django.views import generic

from . import views


app_name = 'polls'
urlpatterns = [
    path('', generic.RedirectView.as_view(url='./question/'), name="index"),
    path('question/', include(views.QuestionViewSet().urls)),
]