"""
    djangotut URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from django.views import generic

from material.frontend import urls as frontend_urls

urlpatterns = [
    path('', generic.RedirectView.as_view(url='/polls/question/'), name='index'),
    path('polls/', include('djangotut.polls.urls', namespace='polls')),
    path('admin/', admin.site.urls),
    path('', include(frontend_urls)),
]
