from random import *
T=["0750","0770","0751","0780"]
R=["112233445566","1122334455","1234567890","1234554321","hama123","hama1234","ahmad123","roman2019","11223344556677","kurd123","rawand12","123456654321","123123","Lina123","kurdup123","mohamed123","ahmed123456","mohammed123","hama1212","kurdistan123","saudi123","hama2004","hamaup21","mahmad123"]
M=[""]
for o in range (10000):
    out = str(randint(0,9999999))
    out2 =(choice(M))
    out3 =(choice(T)+out)
    out4 =(choice(R)+out2)
    print(out3 +":"+ out4)