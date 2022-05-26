AIRFORCE_TYPE_CHOICE = (
    ( 0 ,  'ไม่ระบุ' ) ,
    ( 1 ,  'ทหารประจำการ' ) ,
    ( 8 ,  'นักเรียนทหาร' ) ,
    ( 2 ,  'พลทหาร' ) ,
    ( 3 ,  'พนง.ราชการ' ) ,
    ( 4 ,  'ลูกจ้างประจำ' ) ,
    ( 5 ,  'ลูกจ้างชั่วคราว' ) ,
    ( 6 ,  'ครอบครัว ทอ.' ) ,
    ( 7 ,  'บุคคลภายนอก' ) ,
)

RIGHT_MEDICAL_TREATMENT_CHOICE = (
    ( 0 ,  'ไม่ระบุ' ) ,
    ( 1 ,  'เบิกจ่ายตรง (กรมบัญชีกลาง)' ) ,
    ( 2 ,  'ประกันสังคม' ) ,
    ( 3 ,  'UC (สปสช.)' ) ,
    ( 4 ,  'เงินสด' ) ,
)

CHOICE_STATUSLEVEL = (
    ( 0 ,  'ไม่ระบุ' ) ,
    ( 1 ,  'ผู้ป่วยสีเขียว' ) ,
    ( 2 ,  'ผู้ป่วยสีเหลือง' ) ,
    ( 3 ,  'ผู้ป่วยสีแดง' ) ,
    # ( 4 ,  'ผู้ป่วยสีแดง' ) ,
    # ( 5 ,  'หายป่วย' ) ,
    # ( 6 ,  'เสียชีวิต' ) ,
    # ( 7 ,  'ผู้ใกล้ชิดเสี่ยงสูง' ) ,
    # ( 8 ,  'ผู้ใกล้ชิดปลอดเชื้อ' ) ,
    # ( 9 ,  'ผู้ใกล้ชิดติดเชื้อ' ) ,
)

TREATMENTCHOICES = (
    ( 0 ,  'ไม่ระบุ'),
    ( 10 ,  'รักษาระยะห่าง'),
    ( 20 ,  'กักตัวอยู่บ้าน'),
    ( 30 ,  'กักตัวรอเตียง'),
    ( 40 ,  'Self Isolation'),
    ( 90 ,  'OPSI (เจอ แจก จบ)'),
    ( 50 ,  'Home Isolation'),
    ( 60 ,  'รพ.สนาม'),
    ( 70 ,  'โรงพยาบาล'),
    ( 80 ,  'ICU'),
    
) 

BLOODGROUP = (
    ( 'A' ,  'A'),
    ( 'B' ,  'B'),
    ( 'AB' ,  'AB'),
    ( 'O' ,  'O'),    
) 

CHOICE_Gender = (
    ( '-' ,  'ไม่ระบุ' ) ,
    ( 'ช' ,  'ชาย' ) ,
    ( 'ญ' ,  'หญิง' ) ,
) 


CHOICE_Rank = (
    ( 30101 ,  'พล.อ.อ.*' ) ,
    ( 30102 ,  'พล.อ.อ.*หญิง' ) ,
    ( 30211 ,  'พล.อ.อ.' ) ,
    ( 30212 ,  'พล.อ.อ.หญิง' ) ,
    ( 30213 ,  'พล.อ.' ) ,
    ( 30221 ,  'พล.อ.ท.' ) ,
    ( 30222 ,  'พล.อ.ท.หญิง' ) ,
    ( 30231 ,  'พล.อ.ต.' ) ,
    ( 30232 ,  'พล.อ.ต.หญิง' ) ,
    ( 30301 ,  'น.อ.(พ)' ) ,
    ( 30302 ,  'น.อ.(พ) หญิง' ) ,
    ( 30410 ,  'พ.อ.' ) ,
    ( 30411 ,  'น.อ.' ) ,
    ( 30412 ,  'น.อ.หญิง' ) ,
    ( 30420 ,  'พ.ท.' ) ,
    ( 30421 ,  'น.ท.' ) ,
    ( 30422 ,  'น.ท.หญิง' ) ,
    ( 30431 ,  'น.ต.' ) ,
    ( 30432 ,  'น.ต.หญิง' ) ,
    ( 30511 ,  'ร.อ.' ) ,
    ( 30512 ,  'ร.อ.หญิง' ) ,
    ( 30521 ,  'ร.ท.' ) ,
    ( 30522 ,  'ร.ท.หญิง' ) ,
    ( 30531 ,  'ร.ต.' ) ,
    ( 30532 ,  'ร.ต.หญิง' ) ,
    ( 30541 ,  'กห.ส.' ) ,
    ( 30542 ,  'กห.ส.หญิง' ) ,
    ( 30611 ,  'พ.อ.อ.(พ)' ) ,
    ( 30612 ,  'พ.อ.อ.(พ) หญิง' ) ,
    ( 30711 ,  'พ.อ.อ.' ) ,
    ( 30712 ,  'พ.อ.อ.หญิง' ) ,
    ( 30721 ,  'พ.อ.ท.' ) ,
    ( 30722 ,  'พ.อ.ท.หญิง' ) ,
    ( 30731 ,  'พ.อ.ต.' ) ,
    ( 30732 ,  'พ.อ.ต.หญิง' ) ,
    ( 30811 ,  'จ.อ.' ) ,
    ( 30812 ,  'จ.อ.หญิง' ) ,
    ( 30821 ,  'จ.ท.' ) ,
    ( 30822 ,  'จ.ท.หญิง' ) ,
    ( 30831 ,  'จ.ต.' ) ,
    ( 30832 ,  'จ.ต.หญิง' ) ,
    ( 30841 ,  'กห.ป.' ) ,
    ( 30842 ,  'กห.ป.หญิง' ) ,
    ( 31411 ,  'น.อ.' ) ,
    ( 31412 ,  'น.อ.หญิง' ) ,
    ( 31421 ,  'น.ท.' ) ,
    ( 31422 ,  'น.ท.หญิง' ) ,
    ( 31431 ,  'น.ต.' ) ,
    ( 31432 ,  'น.ต.หญิง' ) ,
    ( 31511 ,  'ร.อ.' ) ,
    ( 31512 ,  'ร.อ.หญิง' ) ,
    ( 31521 ,  'ร.ท.' ) ,
    ( 31522 ,  'ร.ท.หญิง' ) ,
    ( 31531 ,  'ร.ต.' ) ,
    ( 31532 ,  'ร.ต.หญิง' ) ,
    ( 40602 ,  'พลฯ'),
    ( 40200 ,  'พนง.อาวุโสหญิง' ) ,
    ( 40201 ,  'พนง.อาวุโส' ) ,
    ( 40400 ,  'พนง.หญิง' ) ,
    ( 40401 ,  'พนง.' ) ,
    ( 40600 ,  'นาย' ) ,
    ( 40601 ,  'นาง' ) ,
    ( 40602 ,  'น.ส.' ) ,
    ( 0 ,  '' )
) 
