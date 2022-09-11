from socketserver import DatagramRequestHandler
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
        data_catalog = CatalogItem.objects.all()
        DatagramRequestHandler = {
                'list_catalog' : data_catalog,
                'nama' : 'Danendra Herdiansyah' 
        }


        return render(request, "katalog.html", DatagramRequestHandler)