from django.views.generic import ListView
from .models import RaceResult


# 【顧客管理】リスト一覧画面
class RaceResultList(ListView):
    model = RaceResult
    template_name = "analysis/race_result_list.html"
    paginate_by = 10  # 1ページあたりに表示する件数
