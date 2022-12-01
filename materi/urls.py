from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.home, name='about'), 
    path('aplikasikekongruenan/', views.aplikasikekongruenan, name='aplikasikekongruenan'),
    path('aplikasikesebangunan/', views.aplikasikesebangunan, name='aplikasikesebangunan'),
    path('appletkekongruenan/', views.appletkekongruenan, name='appletkekongruenan'),
    path('appletkubus/', views.appletkubus, name='appletkubus'),
    path('appletlingkaran/', views.appletlingkaran, name='appletlingkaran'),
    path('applettranslasi/', views.applettranslasi, name='applettranslasi'),
    path('balok/', views.balok, name='balok'),
    path('dilatasi/', views.dilatasi, name='dilatasi'),
    path('home/', views.home, name='home'),
    path('kekongruenan/', views.kekongruenan, name='kekongruenan'),
    path('kesebangunan/', views.kesebangunan, name='kesebangunan'),
    path('kubus/', views.kubus, name='kubus'),
    path('limas/', views.limas, name='limas'),
    path('lingkaran/', views.lingkaran, name='lingkaran'),
    path('mahasiswa/', views.mahasiswa, name='mahasiswa'),
    path('persamaangarissinggung/', views.persamaangarissinggung, name='persamaangarissinggung'),
    path('persamaanlingkaran/', views.persamaanlingkaran, name='persamaanlingkaran'),
    path('prisma/', views.prisma, name='prisma'),
    path('refleksi/', views.refleksi, name='refleksi'),
    path('rotasi/', views.rotasi, name='rotasi'),
    path('translasi/', views.translasi, name='translasi'),
    
]