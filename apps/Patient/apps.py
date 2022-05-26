from django.apps import AppConfig


class PatientConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Patient'
    verbose_name = "ข้อมูลผู้ป่วย"    
