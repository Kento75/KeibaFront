from django.urls import path
from . import views

app_name = 'prediction'

urlpatterns = [
    path('', views.race_index, name='race_index'),
    path('<year>/<month>/<day>/<venue_no>/', views.venue_race_info, name='venue_race_info'),
]
