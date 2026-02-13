from .models import Operation, Alert, Technician

def get_available_technician():
    tech = Technician.objects.filter(available=True).first()
    return tech

def check_operations(machine):
    latest = Operation.objects.filter(machine=machine).order_by('-created_at').first()
    
    if latest.temperature > 80:
        severity = 1
        message = "High Temperature"

    elif latest.temperature > 65 and latest.temperature < 80:
        severity = 0
        message = "Moderate0 Temperature"

    elif latest.vibration > 50:
        severity = 0
        message = "Moderate Vibration"

    else:
        return None

    tech = get_available_technician()
    alert = Alert.objects.create(
        machine=machine,
        technician=tech,
        message=message,
        severity=severity
    )

    if tech:
        tech.available = False
        tech.save()

    return alert