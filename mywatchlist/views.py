from multiprocessing import context
from socketserver import DatagramRequestHandler
from django.shortcuts import render
from mywatchlist.models import MyWatchlistItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist = MyWatchlistItem.objects.all()
    status_watchlist = ""

    # Referensi : https://docs.djangoproject.com/en/4.1/ref/models/querysets/#django.db.models.query.QuerySet.count
    if MyWatchlistItem.objects.filter(status_watched_film = True).count()>= MyWatchlistItem.objects.filter(status_watched_film = False).count():
        status_watchlist = "Selamat, kamu sudah banyak menonton!"
    else:
        status_watchlist = "Wah, kamu masih sedikit menonton!"

    DatagramRequestHandle = {
        'list_watchlist' : data_watchlist,
        'nama' : 'Danendra Herdiansyah',
        'status_watchlist' : status_watchlist
    }
    return render(request, "mywatchlist.html", DatagramRequestHandle)

# Mengembalikan data berbentuk XML
def show_watchlist_xml(request):
    data_watchlist = MyWatchlistItem.objects.all()


    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

# Mengembalikan data berbentuk JSON
def show_watchlist_json(request):
    data_watchlist = MyWatchlistItem.objects.all()

    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")

# Mengembalikan data berdasarkan ID terhadap XML/JSON
def show_watchlist_xml_by_id(request, id):
    data_watchlist = MyWatchlistItem.objects.filter(pk=id)
    
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_watchlist_json_by_id(request, id):
    data_watchlist = MyWatchlistItem.objects.filter(pk=id)
    
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")