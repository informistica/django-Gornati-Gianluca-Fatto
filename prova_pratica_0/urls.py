from django.urls import path
from prova_pratica_0.views import index0,somma,media

app_name="prova_pratica_0"
urlpatterns=[
  path('',index0, name='index0'),
  path('view_a',somma,name='somma'),
  path('view_b',media,name='media'),
 
]