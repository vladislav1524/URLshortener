from django.urls import path
from . import views


app_name = 'url'

urlpatterns = [
    path('', views.urlShort, name='urlShort'),
    path('u/<slug:slug>/', views.urlRedirect, name='redirect'),
]
