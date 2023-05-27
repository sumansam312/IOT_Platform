from django.contrib import admin
from .models import ApiModel, CircuitModel, CircuitStatusModel

admin.site.register(CircuitModel)
admin.site.register(CircuitStatusModel)
admin.site.register(ApiModel)