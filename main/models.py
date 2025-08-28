from django.db import models
from django.core.validators import MinValueValidator
from users.models import *
class Suv(models.Model):
    brend = models.CharField(max_length=255)
    narx = models.FloatField(validators=[MinValueValidator(0.0)])
    litr = models.PositiveSmallIntegerField()
    batafsil = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.brend

class Mijoz(models.Model):
    ism = models.CharField(max_length=255)
    tel_raqam = models.CharField(max_length=15)
    manzil = models.CharField(max_length=255)
    qarz = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.ism

class Haydovchi(models.Model):
    ism = models.CharField(max_length=255)
    tel_raqam = models.CharField(max_length=15)
    smena= models.CharField(max_length=50)

    def __str__(self):
        return self.ism

class Buyurtma(models.Model):
    suv_id = models.ForeignKey(Suv, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    mijoz_id = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.FloatField(validators=[MinValueValidator(0.0)])
    umumiy_narx = models.FloatField(validators=[MinValueValidator(0.0)])
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

