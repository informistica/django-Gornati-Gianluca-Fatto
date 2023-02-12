from django.urls import path
from .views import home, ArticoloDetailViewCB,ArticoloListView,GiornalistaDetailViewCB,GiornalistaListView,giornalisti_list_api,articoli_list_api, giornalista_api,articolo_api #articoloDetailView

app_name="news"

urlpatterns = [
    path('', home, name="homeview"),
    #path('articoli/<int:pk>',articoloDetailView,name="articolo_detail"),
    path('articoli/<int:pk>',ArticoloDetailViewCB.as_view(),name="articolo_detail"),
    path('lista_articoli/',ArticoloListView.as_view(),name="lista_articoli"),
    path('giornalisti/<int:pk>',GiornalistaDetailViewCB.as_view(),name="giornalista_detail"),
    path('lista_giornalisti/',GiornalistaListView.as_view(),name="lista_giornalisti"),
    path('lista_giornalisti_api/',giornalisti_list_api,name="lista_giornalisti_api"),
    path('lista_articoli_api/',articoli_list_api,name="lista_articoli_api"),
    path('giornalista_api/<int:pk>', giornalista_api,name="giornalista_api"),
    path('articolo_api/<int:pk>', articolo_api,name="articolo_api"),

   

]
