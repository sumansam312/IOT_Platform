from django.db import models
from django.contrib.auth.models import User

class CircuitModel(models.Model):
    led_1 = models.BooleanField(default=False)
    led_2 = models.BooleanField(default=False)
    doc = models.DateTimeField(auto_now_add=True)
    doe = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.doc}'
    

class CircuitStatusModel(models.Model):
    led_1 = models.BooleanField(default=False)
    led_2 = models.BooleanField(default=False)
    doc = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doc} - {self.led_1} - {self.led_2}'
    

class ApiModel(models.Model):
    write_api = models.CharField(max_length=10)
    read_api = models.CharField(max_length=10)

    def __str__(self):
        return self.write_api