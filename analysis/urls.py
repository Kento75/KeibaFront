from django.urls import path
from .views import RaceResultList


app_name = 'analysis'

urlpatterns = [
    path('', RaceResultList.as_view(), name='race_result_list'),        # レース結果一覧画面へ遷移
]
