# Generated by Django 4.1 on 2022-09-21 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0003_rename_mywishlistitem_mywatchlistitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlistitem',
            name='rating_film',
            field=models.CharField(max_length=50),
        ),
    ]
