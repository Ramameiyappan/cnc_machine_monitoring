from django.db import models

class Machine(models.Model):
    STATUS_CHOICES = [
        ('running', 'Running'),
        ('stopped', 'Stopped'),
    ]

    name = models.CharField(max_length=20, unique=True)
    machine_type = models.CharField(max_length=15)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='running')
    last_active = models.DateTimeField(auto_now=True)

class Technician(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    available = models.BooleanField(default=True)
    
class Operation(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    temperature = models.FloatField()
    vibration = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class Alert(models.Model):
    SEVERITY = [
        (0, 'Low'),
        (1, 'High'),
    ]

    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.SET_NULL, null=True, blank=True )
    message = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True, blank=True)