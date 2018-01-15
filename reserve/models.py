from django.db import models

# Create your models here.
class Patient(models.Model):
    SEX_CHOICES = (
        (0, 'Man'),
        (1, 'Woman'),
    )

    pid = models.IntegerField()
    pname = models.CharField(max_length=20)
    pnamekana = models.CharField(max_length=50)
    birthdate = models.DateField()
    psex = models.IntegerField(choices=SEX_CHOICES)
    memo = models.TextField()

class Reserve(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,blank=True,null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    memo = models.TextField()
