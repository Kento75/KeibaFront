from django.shortcuts import render
from .models import race_data


# レース一覧(該当週)画面
def race_index(request):
    race_lists = race_data.objects.order_by('date')
    return render(request, 'prediction/race_index.html',
                  {'race_lists': race_lists})
