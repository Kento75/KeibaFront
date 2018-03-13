from django.urls import path
from . import views


urlpatterns = [
    path('prediction/', views.race_index, name='race_index'),
]
