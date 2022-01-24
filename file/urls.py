from django.urls import path
from . import views
app_name = 'file'
urlpatterns = [
    path('upload1/', views.upload1, name='upload1'),
]