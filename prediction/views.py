from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import race_data, race_master


# レース一覧(該当週)画面
def race_index(request):

    venue_lists = race_master.objects.filter(date='').values('venue').annotate(Count('venue')).order_by('venue')
    race_lists = race_master.objects.all().order_by('date').order_by('venue')
    context = {
        'race_lists': race_lists,
        'venue_lists': venue_lists,
    }
    return render(request, 'prediction/race_index.html', context)


# 開催日・開催地レース情報画面
def venue_race_info(request, pk):
    obj = get_object_or_404(race_data, pk=pk)
    return render(request, 'prediction/venue_race_info.html', {
        'race_data_lists': obj,
    })
