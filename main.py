import random

a = "abcdefgğhıijklmnoöprsştuüvyz1234567890*-/-+,.<>|£#$½{[]}é"

uzunlug = int(input("şifrə uzunluğunu daxil edin: "))

sifre=""
for i in range(uzunlug):
    sifre += random.choice(a)
    
print(sifre)
