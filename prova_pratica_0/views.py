from django.shortcuts import render
import random


# Create your views here.
def index0(request):
    return render(request,"index0.html")

def somma(request):
    n1=random.randint(1,11)
    n2=random.randint(1,11)
    context={'n1':n1,'n2':n2,'somma':n1+n2}
    return render(request,"somma.html",context)

def media(request):
    lista=[]
    l1=['a','b','c']
    somma=0
    for i in range(1,26):
        num=random.randint(1,11)
        somma+=num
        lista.append(num)
    media=somma/25
    context={'lista':lista,'media':media,'l1':l1,'oggetto':{'nome':'mauro','cognome':'spina'}}
    return render(request,"media.html",context)
  