from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import race_data


# レース一覧(該当週)画面
def race_index(request):

    date_lists = race_data.objects\
        .values('date', 'year', 'month', 'day').annotate(Count('date'))

    race_lists = race_data.objects\
        .values('date', 'venue', 'venue_number', 'year', 'month', 'day').annotate(Count('date'))

    context = {
        'date_lists': date_lists,
        'race_lists': race_lists,
    }
    return render(request, 'prediction/race_index.html', context)


# 開催日・開催地レース情報画面
def venue_race_info(request, year, month, day, venue_no):
    obj = get_object_or_404(race_data, year=year, month=month, day=day, venue_number=venue_no)
    context = {
        'race_data_lists': obj,
    }
    return render(request, 'prediction/venue_race_info.html', context)
