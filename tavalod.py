temp=input('dariaft trikhtavalod')
tavalod=int(temp)
if tavalod<1250:
    print('tarikh eshtebah ast')
    exit()   
age=1403-tavalod
if age<30:
    print('javan')
    exit()
if age >30 and age<60 :   
    print('miansal') 
    exit()
if age>50:
    print('pir')
    exit()
     
