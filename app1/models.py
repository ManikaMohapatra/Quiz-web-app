from django.db import models

class GkQuiz(models.Model):
    Question=models.CharField(max_length=1000)
    Option1=models.CharField(max_length=200)
    Option2 = models.CharField(max_length=200)
    Option3 = models.CharField(max_length=200)
    Option4 = models.CharField(max_length=200)
    Corrans=models.CharField(max_length=200)
class ScienceQuiz(models.Model):
    Question=models.CharField(max_length=1000)
    Option1=models.CharField(max_length=200)
    Option2 = models.CharField(max_length=200)
    Option3 = models.CharField(max_length=200)
    Option4 = models.CharField(max_length=200)
    Corrans=models.CharField(max_length=200)
class SportsQuiz(models.Model):
    Question=models.CharField(max_length=1000)
    Option1=models.CharField(max_length=200)
    Option2 = models.CharField(max_length=200)
    Option3 = models.CharField(max_length=200)
    Option4 = models.CharField(max_length=200)
    Corrans=models.CharField(max_length=200)




