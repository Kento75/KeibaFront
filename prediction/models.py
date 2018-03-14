from django.db import models


# レース予測データ格納用テーブル
# テーブル名：prediction_race_data
class race_data(models.Model):
    date = models.CharField(max_length=20)
    venue = models.CharField(max_length=20)
    race_number = models.SmallIntegerField()
    race_name = models.CharField(max_length=255)
    frame_number = models.SmallIntegerField()
    horse_number = models.SmallIntegerField()
    horse_name = models.CharField(max_length=255)
    top3_flg = models.BooleanField()
    top3_ratio = models.FloatField()

    # todo 日付・場所ごとのレース数をカウントする処理に変更する
    def get_race_count(self):
        race_counts = self.race_number
        return race_counts
