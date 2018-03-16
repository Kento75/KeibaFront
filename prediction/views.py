from django.shortcuts import render
from django.db.models import Count
from .models import race_data, race_master


# レース一覧(該当週)画面
def race_index(request):

#    race_lists = race_data.objects.values('date').annotate(Count('date')).order_by('date')
    venue_lists = race_master.objects.filter(date='').values('venue').annotate(Count('venue')).order_by('venue')
    race_lists = race_master.objects.all().order_by('date').order_by('venue')
    context = {
        'race_lists': race_lists,
        'venue_lists': venue_lists,
    }
    return render(request, 'prediction/race_index.html', context)
