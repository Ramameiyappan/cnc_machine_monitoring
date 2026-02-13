from django.contrib import admin
from .models import Machine, Operation, Alert, Technician

admin.site.register(Machine)
admin.site.register(Operation)
admin.site.register(Alert)
admin.site.register(Technician)
