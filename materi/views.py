from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . models import Mahasiswa

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
def aplikasikekongruenan(request):
    template = loader.get_template('aplikasikekongruenan.html')
    return HttpResponse(template.render())
def aplikasikesebangunan(request):
    template = loader.get_template('aplikasikesebangunan.html')
    return HttpResponse(template.render())
def appletkekongruenan(request):
    template = loader.get_template('appletkekongruenan.html')
    return HttpResponse(template.render())
def appletkubus(request):
    template = loader.get_template('appletkubus.html')
    return HttpResponse(template.render())
def appletlingkaran(request):
    template = loader.get_template('appletlingkaran.html')
    return HttpResponse(template.render())
def applettranslasi(request):
    template = loader.get_template('applettranslasi.html')
    return HttpResponse(template.render())
def balok(request):
    template = loader.get_template('balok.html')
    return HttpResponse(template.render())
def dilatasi(request):
    template = loader.get_template('dilatasi.html')
    return HttpResponse(template.render())
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def kekongruenan(request):
    template = loader.get_template('kekongruenan.html')
    return HttpResponse(template.render())
def kesebangunan(request):
    template = loader.get_template('kesebangunan.html')
    return HttpResponse(template.render())
def kubus(request):
    template = loader.get_template('kubus.html')
    return HttpResponse(template.render())
def limas(request):
    template = loader.get_template('limas.html')
    return HttpResponse(template.render())
def lingkaran(request):
    template = loader.get_template('lingkaran.html')
    return HttpResponse(template.render())
def mahasiswa(request):
    template = loader.get_template('mahasiswa.html')
    return HttpResponse(template.render())
def persamaangarissinggung(request):
    template = loader.get_template('persamaangarissinggung.html')
    return HttpResponse(template.render())
def persamaanlingkaran(request):
    template = loader.get_template('persamaanlingkaran.html')
    return HttpResponse(template.render())
def prisma(request):
    template = loader.get_template('prisma.html')
    return HttpResponse(template.render())
def refleksi(request):
    template = loader.get_template('refleksi.html')
    return HttpResponse(template.render())
def rotasi(request):
    template = loader.get_template('rotasi.html')
    return HttpResponse(template.render())
def translasi(request):
    template = loader.get_template('translasi.html')
    return HttpResponse(template.render())