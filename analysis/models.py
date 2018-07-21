from django.db import models


# レース予測データ格納用テーブル
# テーブル名：analysis_race_result
class RaceResult(models.Model):
    date = models.CharField(max_length=10, null=False)  # yyyy/MM/dd形式の文字列型
    venue = models.CharField(max_length=20)
    race_number = models.SmallIntegerField()
    race_name = models.CharField(max_length=255)
    order_of_finish = models.SmallIntegerField()
    frame_number = models.SmallIntegerField()
    horse_number = models.SmallIntegerField()
    horse_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=2)
    age = models.SmallIntegerField()
    time_g = models.FloatField()
    horse_weight = models.FloatField()
    margin = models.CharField(max_length=20)
    time_3f = models.FloatField()
    jockey_name = models.CharField(max_length=50)
    load_weight = models.FloatField()
    odds_order = models.SmallIntegerField()
    odds = models.FloatField()
    trainer_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'analysis_race_result'

