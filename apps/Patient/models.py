from cProfile import label
from datetime import date
import datetime

from django.db import models

# Create your models here.
from apps.UserData.models import User, Unit
from .choices import (AIRFORCE_TYPE_CHOICE, RIGHT_MEDICAL_TREATMENT_CHOICE, 
                      CHOICE_STATUSLEVEL, TREATMENTCHOICES, CHOICE_Gender, 
                      BLOODGROUP, CHOICE_Rank)

class Patient(models.Model):
    class Meta:
        verbose_name_plural = "ตารางผู้ป่วย [Patient]"    
        # ordering = ('-ActionOccure', 'ActionUser', 'ActionDo')
    
    date = models.DateField(verbose_name = 'วันที่', default=datetime.date.today)
    rank = models.PositiveIntegerField(verbose_name="ยศ", choices = CHOICE_Rank, default = 0, null=True, blank=True)
    full_name = models.CharField(verbose_name = 'ชื่อผู้ป่วย', max_length = 150)
    gender = models.CharField(verbose_name = 'เพศ', max_length = 2, choices = CHOICE_Gender, default = 'ช', null=True, blank = True)
    birth_day  = models.DateField(verbose_name = 'วันเกิด', null = True, blank = True)
    person_id = models.CharField(verbose_name = 'เลขบัตรประชาชน', max_length = 13, unique = True)    
    unit =  models.ForeignKey(Unit, verbose_name="สังกัด", on_delete=models.SET_NULL, null = True, blank=False, related_name='CurrentUnit')
    airforce_type = models.IntegerField(verbose_name = 'ประเภทข้าราชการ', choices = AIRFORCE_TYPE_CHOICE, default = 0, null=True, blank = True)                             
    
    
    blood_group = models.CharField(verbose_name = 'หมู่เลือด', max_length = 3, choices = BLOODGROUP, default = 0, null=True, blank = True)                                                         
    height = models.IntegerField(verbose_name = 'ส่วนสูง', null = True)                                                         
    weight = models.IntegerField(verbose_name = 'น้ำหนัก', null = True)                                                         
    disease = models.CharField(verbose_name = 'โรคประจำตัว', max_length = 100, null = True, blank = True)
    drug_allergy  = models.CharField(verbose_name = 'ประวัติการแพ้ยา', max_length = 100, blank = True,  null = True)    

    atk_date  = models.DateField(verbose_name = 'วันตรวจ ATK', blank = True, null = True,)
    rt_pcr  = models.DateField(verbose_name = 'วันตรวจ RT PCR', blank = True, null = True,)
    rt_pcr_place  = models.CharField(verbose_name = 'สถานที่ตรวจ RT PCR', max_length = 50, blank = True, null = True,)
    atk_place  = models.CharField(verbose_name = 'สถานที่ตรวจ ATK', max_length = 50, blank = True, null = True,)
    status = models.IntegerField(verbose_name = 'สถานะผู้ป่วยปัจจุบัน', choices = CHOICE_STATUSLEVEL[0:4], default = 0, null=True, blank = True)
    treatment = models.IntegerField(verbose_name = 'การรักษาปัจจุบัน', choices = TREATMENTCHOICES, default = 0, null=True, blank = True)                                                         
    symptom = models.TextField(verbose_name = 'อาการ', null = True, blank = True)
    
    mobile  = models.CharField(verbose_name = 'เบอร์มือถือ', max_length = 20)
    address = models.TextField(verbose_name = 'ที่อยู่ปัจจุบัน', null = True, blank = True)
    right_medical = models.IntegerField(verbose_name = 'สิทธิ์การรักษาพยาบาล', choices = RIGHT_MEDICAL_TREATMENT_CHOICE, default = 0, null = True, blank = False)

    emergency_name = models.CharField(verbose_name = 'ผู้ติดต่อฉุกเฉิน', max_length = 150, null = True)
    emergency_mobile  = models.CharField(verbose_name = 'เบอร์ฉุกเฉิน', max_length = 20, null = True)
                                
    comment  = models.TextField(verbose_name = "หมายเหตุ", default = None, blank = True, null = True, )

    document_approved = models.BooleanField(verbose_name = "มีใบวิทยุ", default = False)
    data_user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='DataUser', blank = True, null = True, verbose_name = 'ผู้บันทึก')

    def __str__(self):
        return self.full_name

    @property
    def Age(self):
        if self.BirthDay:
            today = date.today()
            return today.year - self.BirthDay.year
        else:
            return "-"
    
