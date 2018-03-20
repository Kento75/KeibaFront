from django.shortcuts import render, get_list_or_404
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
    obj = get_list_or_404(RaceData.objects
                          .values('date', 'year', 'month', 'day',
                                  'venue_number', 'venue', 'race_number', 'race_name')
                          .annotate(Count('race_number')).order_by('race_number'),
                          year=year, month=month, day=day, venue_number=venue_no)
    context = {
        'race_data_lists': obj,
    }
    return render(request, 'prediction/venue_race_info.html', context)


# レース詳細情報画面
def race_detail(request, year, month, day, venue_no, race_no):
    obj = get_list_or_404(RaceData.objects.all().order_by('horse_number'),
                          year=year, month=month, day=day, venue_number=venue_no, race_number=race_no)
    context = {
        'race_detail_lists': obj,
    }
    return render(request, 'prediction/race_detail.html', context)


# SQL確認用
def show_select_sql(queryset):
    compiler = queryset.query.get_compiler(using=queryset.db)
    return compiler.as_sql()
