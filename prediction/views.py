from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import RaceData


# レース一覧(該当週)画面
def race_index(request):

    date_lists = RaceData.objects\
        .values('date', 'year', 'month', 'day').annotate(Count('date'))

    race_lists = RaceData.objects\
        .values('date', 'venue', 'venue_number', 'year', 'month', 'day').annotate(Count('date'))

    context = {
        'date_lists': date_lists,
        'race_lists': race_lists,
    }
    return render(request, 'prediction/race_index.html', context)


# 開催日・開催地レース情報画面
def venue_race_info(request, year, month, day, venue_no):
    obj = get_object_or_404(RaceData.objects
                            .defer('frame_number', 'horse_number', 'horse_name', 'top3_flg', 'top3_ratio')
                            .annotate(Count('race_number')).order_by('race_number'),
                            year=year, month=month, day=day, venue_number=venue_no)
    context = {
        'race_data_lists': obj,
    }
    return render(request, 'prediction/venue_race_info.html', context)


def show_select_sql(queryset):
    compiler = queryset.query.get_compiler(using=queryset.db)
    return compiler.as_sql()