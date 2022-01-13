from django.contrib import admin

# Register your models here.
from .models import Voto, Studente, Assenza,Materia

admin.site.register(Voto)
admin.site.register(Studente)
admin.site.register(Materia)
admin.site.register(Assenza)