print ("""
*********************
    ATM MACHINE 
     NICOSIA
     
CHOOSE YOUR OPERATION . 

1. DEPOSIT
2. CASH WITHDRAWL
3. BALANCE 
4. QUIT 

*********************
""")
sys_kullanici ="alara02"
sys_parola = "1234"
kullaniciadi = input("USERNAME  : ")
parola = input("parola : ")
balance = 4000
if (sys_kullanici==kullaniciadi and sys_parola!=parola):
    print ("Parola is not correct !.")
elif (sys_kullanici!=kullaniciadi and sys_parola==parola):
    print("username is not correct .")
elif (sys_kullanici!=kullaniciadi and sys_parola!=parola):
    print("username and parola is not correct.")
else :
    print("Welcome the system..")
    
islem = int (input("Sign your operation : "))
if islem == 1:
    a = input ("Enter the Deposit ")
    a = int(a)
    print ("New Ballance {}".format(a+balance))
if islem==2:
    b = input ("Enter the amount : ")
    b = int(b)
    if b > balance:
        print ("Your balace not enough")
    else:
        print ("New Balance : {}" .format(balance-b))
    
if islem==3:
    print ("Balance : {}".format (balance))
    
if islem==4:
    print ("See You Later :)")
   
    
       
       
       
