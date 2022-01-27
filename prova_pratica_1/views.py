from django.shortcuts import render
from .models import Studente, Materia, Assenza, Voto

# Create your views here.
def view_b(request):
  materie = Materia.objects.all()
  context={}
  context['materie']=materie
  return render(request,"view_b.html",context)
  
def view_c(request):
  studenti=Studente.objects.all()
  materie=Materia.objects.all()
  votiTutti={}
  for studente in studenti:
    ris=[]
    for materia in materie:
      voti=Voto.objects.filter(studente=studente,materia=materia)
      somma=0.0
      if len(voti)!=0:
        for voto in voti:
          somma+=voto.valore
        somma/=len(voti)
      assenze=Assenza.objects.filter(studente=studente,materia=materia)
      somma2=0.0
      if len(assenze)!=0:
        for assenza in assenze:
          somma2+=assenza.valore
        somma2/=len(assenze)
      ris.append((materia,somma,somma2))
    votiTutti[studente.nome+ " "+studente.cognome]=ris
  context={}
  context['voti']=votiTutti
  print(votiTutti)
  return render(request,"view_c.html",context)
  
def view_c2(request):
  studenti=Studente.objects.all()
  materie=Materia.objects.all()
  votiTutti={}
  for studente in studenti:
    ris=[]
    for materia in materie:
      voti=Voto.objects.filter(studente=studente,materia=materia)
      somma=0.0
      if len(voti)!=0:
        for voto in voti:
          somma+=voto.valore
        somma/=len(voti)
      assenze=Assenza.objects.filter(studente=studente,materia=materia)
      somma2=0.0
      if len(assenze)!=0:
        for assenza in assenze:
          somma2+=assenza.valore
      ris.append((materia,somma,somma2))
    votiTutti[studente.nome+ " "+studente.cognome]=ris
  context={}
  context['voti']=votiTutti
  print(votiTutti)
  return render(request,"view_c2.html",context)
  
def view_c3a(request):
  studenti=Studente.objects.all()
  materie=Materia.objects.all()
  votiTutti={}
  for studente in studenti:
    ris=[]
    for materia in materie:
      voti=Voto.objects.filter(studente=studente,materia=materia)
      somma=0.0
      if len(voti)!=0:
        for voto in voti:
          somma+=voto.valore
        somma/=len(voti)
      assenze=Assenza.objects.filter(studente=studente,materia=materia)
      somma2=0.0
      if len(assenze)!=0:
        for assenza in assenze:
          somma2+=assenza.valore
      ris.append((materia,somma,somma2,))
      ris.append(studente.id)
    votiTutti[studente.nome+ " "+studente.cognome]=ris
  context={}
  context['voti']=votiTutti
  print(votiTutti)
  return render(request,"view_c3a.html",context)
  
def view_c3b(request, studente):
  alunno=Studente.objects.get(id=studente)
  materie=Materia.objects.all()
  votiTutti={}
  ris=[]
  for materia in materie:
    voti=Voto.objects.filter(studente=studente,materia=materia)
    somma=0.0
    if len(voti)!=0:
      for voto in voti:
        somma+=voto.valore
      somma/=len(voti)
    assenze=Assenza.objects.filter(studente=studente,materia=materia)
    somma2=0.0
    if len(assenze)!=0:
      for assenza in assenze:
        somma2+=assenza.valore
    ris.append((materia,somma,somma2))
  context={}
  context['voti']=ris
  context['studente']=alunno
  print(votiTutti)
  return render(request,"view_c3b.html",context)