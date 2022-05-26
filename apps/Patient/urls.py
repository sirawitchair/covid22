from django.urls import path

from .views import PatientCreateView, PatientListView, RadioDocument,updateDocument,RadioWorkbook

app_name = 'Patient'
urlpatterns = [
    path('pcv', PatientCreateView.as_view(), name = "CreateNew"),
    path('', PatientListView.as_view(), name = "List"),
    path('rd/<patient_id>', RadioDocument, name = "RadioDocument"),
    path('rw', RadioWorkbook, name = "RadioWorkbook"),
    path('edit/<patient_id>',updateDocument, name='updateDocument'),
]
