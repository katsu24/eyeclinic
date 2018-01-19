from django.db import models

# Create your models here.
class Patient(models.Model):
    SEX_CHOICES = (
        (0, '男'),
        (1, '女'),
    )

    pid = models.IntegerField()
    pname = models.CharField(max_length=20)
    pnamekana = models.CharField(max_length=50)
    birthdate = models.DateField()
    psex = models.IntegerField(choices=SEX_CHOICES)
    memo = models.TextField()

    def __str__(self):
        return self.pnamekana

class Reserve(models.Model): 
    RESERVE_TYPE = (
        (0, '手術'),
        (1, '検査'),
        (2, '術前検査'),
        (3, '診察'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reserve_type = models.IntegerField(choices=RESERVE_TYPE, blank=True, null=True)
    memo = models.TextField()

    def __str__(self):
        return self.id
