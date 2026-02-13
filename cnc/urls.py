from django.urls import path

from .views import OperationAPIView, TechnicianAPIView, MachineAPIView, ResolveAlertAPIView, AlertAPIView, Dashboard

urlpatterns = [
    path('machines/', MachineAPIView.as_view()),
    path('technician/', TechnicianAPIView.as_view()),
    path('operation/', OperationAPIView.as_view()),
    path('alert/', AlertAPIView.as_view()),
    path('alert/resolve/<int:alert_id>/', ResolveAlertAPIView.as_view()),
    path('', Dashboard.as_view()),
]
