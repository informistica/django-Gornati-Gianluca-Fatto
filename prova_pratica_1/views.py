from django.shortcuts import render

# Create your views here.
def view_b(request):
  materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
  context={}
  context['materie']=materie
  return render(request,"view_b.html",context)
  
def view_c(request):
  voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7.5,2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]}
  context={}
  context['voti']=voti
  return render(request,"view_c.html",context)