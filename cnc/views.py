from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Machine, Technician, Alert
from django.utils import timezone
from .serializers import OperationSerializer, MachineSerializer, TechnicianSerializer, AlertSerializer
from .tasks import check_operations

class MachineAPIView(APIView):
    def get(self, request):
        machines = Machine.objects.all()
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)
     
    def post(self, request):
        serializer = MachineSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Machine created"},
            status=201
        )
    
class TechnicianAPIView(APIView):
    def get(self, request):
        techs = Technician.objects.all()
        serializer = TechnicianSerializer(techs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TechnicianSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tech = serializer.save()
        
        pending = Alert.objects.filter(technician=None, resolved=False ).order_by('-severity')
        for alert in pending:
            alert.technician = tech
            alert.save()

            tech.available = False
            tech.save()
            break

        return Response(
            {"message": "Technician created"},
            status=201
        )

class OperationAPIView(APIView):
    def post(self, request):
        serializer = OperationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        operation = serializer.save()
        check_operations(operation.machine)
        return Response(
            {"message": "operation received"},
            status=status.HTTP_201_CREATED
        )

class ResolveAlertAPIView(APIView):
    def post(self, request, alert_id):
        try:
            alert = Alert.objects.get(id=alert_id)
            alert.resolved = True
            alert.resolved_at = timezone.now()
            tech = alert.technician
            alert.save()

            if tech:
                tech.available = True
                tech.save()

            alert.machine.status = "running"
            alert.machine.save()

            return Response({
                "message": "Alert Resolved"
            })

        except Alert.DoesNotExist:
            return Response({
                "error": "Alert Not Found"
            }, status=404)
        
class AlertAPIView(APIView):
    def get(self, request):
        alerts = Alert.objects.filter(resolved=False).order_by(
            '-severity',
            '-created_at'
        )
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)

class Dashboard(APIView):
    def get(self, request):
        machines = Machine.objects.all()
        alerts = Alert.objects.filter(resolved=False).order_by('-severity')
        techs = Technician.objects.all()

        return render(request, 'dashboard.html', {
            "machines": machines,
            "alerts": alerts,
            "techs": techs
        })