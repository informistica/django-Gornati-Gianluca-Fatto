from django.db import models

# Create your models here.
class Materia(models.Model):
  nome=models.TextField(max_length=50)
  def __str__(self):
    return self.nome
  
class Studente(models.Model):
  nome=models.TextField(max_length=50)
  cognome=models.TextField(max_length=50)
  def __str__(self):
    return self.nome + " "+self.cognome
class Voto(models.Model):
  studente=models.ForeignKey(Studente,on_delete=models.CASCADE)
  materia=models.ForeignKey(Materia,on_delete=models.CASCADE)
  valore=models.FloatField()
  def __str__(self):
    return self.studente.__str__()+" "+self.materia.__str__()+" "+str(self.valore)
  
class Assenza(models.Model):
  studente=models.ForeignKey(Studente,on_delete=models.CASCADE)
  materia=models.ForeignKey(Materia,on_delete=models.CASCADE)
  valore=models.IntegerField()
  def __str__(self):
    return self.studente.__str__()+" "+self.materia.__str__()+" "+str(self.valore)
  