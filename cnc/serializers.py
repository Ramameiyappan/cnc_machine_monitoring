from rest_framework import serializers
from .models import Machine, Operation, Alert, Technician

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = "__all__"

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = "__all__"

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = "__all__"
