from django.urls import path
from .views import view_b, view_c, view_c2, view_c3a, view_c3b
app_name="prova_pratica_1"
urlpatterns=[
  path('view_b',view_b, name='view_b'),
  path('view_c',view_c,name='view_c'),
  path('view_c2',view_c2,name='view_c2'),
  path('view_c3a',view_c3a,name='view_c3a'),
  path('view_c3b/<int:studente>',view_c3b,name='view_c3b'),
]