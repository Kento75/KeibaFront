from django.db import models


# レース予測データ格納用テーブル
# テーブル名：prediction_race_data
class race_data(models.Model):
    date = models.CharField(max_length=10, null=False)  # yyyy/MM/dd形式の文字列型
    year = models.CharField(max_length=4, null=False)
    month = models.CharField(max_length=2, null=False)
    day = models.CharField(max_length=2, null=False)
    venue_number = models.CharField(max_length=2, null=False)
    venue = models.CharField(max_length=20)
    race_number = models.SmallIntegerField()
    race_name = models.CharField(max_length=255)
    frame_number = models.SmallIntegerField()
    horse_number = models.SmallIntegerField()
    horse_name = models.CharField(max_length=255)
    top3_flg = models.BooleanField()
    top3_ratio = models.FloatField()
