import datetime
import re

from django.db import models
from django.contrib.auth.models import AbstractUser, Group

from .constants import RTAFUnitSection, CHOICE_Rank




class Unit(models.Model):

    class Meta:
        verbose_name_plural = "1. หน่วยขึ้นตรง ทอ."     
    short_name = models.CharField(max_length = 20, blank = False)
    full_name  = models.CharField(max_length = 90, blank = False)    

    def __str__(self):
        return f'{self.short_name}'


class User(AbstractUser):
    class Meta:        
        verbose_name_plural = "2. ผู้ใช้งานระบบ"         
        # permissions = USER_PERMISSION

    af_id = models.CharField(verbose_name = "เลขประจำตัว ทอ.", max_length = 15, null = True)
    person_id = models.CharField(verbose_name="เลขบัตรประชาชน", max_length = 13, null=True, blank=True, default = '' )
    rank = models.PositiveIntegerField(verbose_name="ยศ", choices = CHOICE_Rank, default = 0, null=True, blank=True)
    position  =  models.CharField(verbose_name="ตำแหน่ง (ย่อ)", max_length=250, null = True, blank = True)
  
    office_phone = models.CharField(verbose_name="เบอร์ที่ทำงาน", max_length = 20, null=True, blank=True)
    mobile_phone = models.CharField(verbose_name="มือถือ", max_length = 30, null=True, blank=True)
    # rtaf_email = models.EmailField(verbose_name = "ที่อยู่ email ทอ.", null=True, blank=True)
    unit =  models.ForeignKey(Unit, verbose_name="สังกัด", on_delete=models.SET_NULL, null = True, blank=True, related_name='current_unit')

    hris_update = models.DateField(verbose_name="update กับ HRIS", null = False, default=datetime.date(2021,5,1))


    def rank_display(self):
        RankDisplay = str(self.get_rank_display())
        if RankDisplay == '':
            return  ''
            
            
        if "ว่าที่" in RankDisplay:
            RankDisplay = RankDisplay[6:]
        elif "กห." in RankDisplay:
            if "หญิง" in RankDisplay:
                RankDisplay = "น.ส."
            else:
                RankDisplay = "นาย"
        elif "พนง." in RankDisplay:
            if "หญิง" in RankDisplay:
                RankDisplay = "น.ส."
            else:
                RankDisplay = "นาย"

        if re.findall("หญิง", RankDisplay ):
            return f'{RankDisplay} '        
        elif re.findall("(พ)", RankDisplay ):
            RankDisplay = RankDisplay.replace("(พ)", "")    
        
        return f'{RankDisplay}'
        
        
    @property
    def ShortName(self):        
        return f'{self.rank_display()}{self.first_name} ฯ'
        
    @property
    def FullName(self):        
        return f'{self.rank_display()}{self.first_name} {self.last_name}'
            
       
    def __str__(self):
        return self.FullName

