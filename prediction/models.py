from django.db import models


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
