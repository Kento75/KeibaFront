from django.urls import path
from . import views


urlpatterns = [
    path('prediction/', views.race_index, name='race_index'),
    path('prediction/<pk>/', views.venue_race_info, name='venue_race_info'),
]
