from django.contrib import admin

from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('date','full_name','mobile', 'unit', 'status', 'document_approved')
    list_display_links = ['full_name']
    list_editable  = ['document_approved',]
    list_filter = ('unit',)
    # ordering = ('-last_login','current_unit','rank',)
    date_hierarchy = 'date'
    # save_as = True
    def get_queryset(self, request):
        qs = super(PatientAdmin, self).get_queryset(request)

        currect_user = request.user
        user_groups = [g.name for g in currect_user.groups.all()]
        qs = Patient.objects.all()
        # if 'COMMANDER' in user_groups or 'DOUser' in  user_groups:            
        #     pass
        # elif 'UnitAdmin' in user_groups:            
        #     qs = Patient.objects.filter(unit = currect_user.unit)
        # else:            
        #     qs = Patient.objects.filter(data_user = currect_user)
        # elif 'MedicalUser' in user_groups:
        #     qs = Patient.objects.filter(document_approved = True)

        # qs = qs.order_by('-date')
        return qs

# Register your models here.
