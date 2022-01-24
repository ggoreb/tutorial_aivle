from django.urls import path
from . import views
app_name = 'paging'
urlpatterns = [
    path('army_shop/', views.army_shop, name='army_shop'),
]