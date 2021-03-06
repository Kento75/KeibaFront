# Generated by Django 2.0.3 on 2018-03-12 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='race_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('venue', models.CharField(max_length=20)),
                ('race_number', models.SmallIntegerField()),
                ('race_name', models.CharField(max_length=255)),
                ('frame_number', models.SmallIntegerField()),
                ('horse_number', models.SmallIntegerField()),
                ('horse_name', models.CharField(max_length=255)),
                ('top3_flg', models.BooleanField()),
                ('top3_ratio', models.FloatField()),
            ],
        ),
    ]
