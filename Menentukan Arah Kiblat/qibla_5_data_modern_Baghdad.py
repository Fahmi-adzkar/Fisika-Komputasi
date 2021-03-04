print('+++++===================================+++++')
print('---Metode Trigonometri Bola Menentukan Arah Kiblat---')
print('---------------------------Baghdad, Iraq---------------------------')
print('------------------Data Koordinat Google Map------------------')
print('--------------+ Oleh : Muhamad Fahmi Adzkar +--------------')
print('--------+++++++ Bandung, 13 Januari 2021 +++++----------')
print('+++++===================================+++++')

from math import *

#Data Koordinat Berdasarkan Google Map
#Lintang Baghdad, Iraq
LB = 33.315228 #Lintang dalam Desimal
Cos_LB = cos(radians (LB)) #Cos Lintang Bandung
Sin_LB = sin(radians (LB)) #Sin Lintang Bandung

#Bujur Baghdad, Iraq
BB = 44.366118 #Bujur dalam Desimal
Sin_BB = sin(radians (BB)) #Sin Bujur Bandung
Cos_BB = cos(radians (BB)) #Cos Bujur Bandung

#Lintang Mekkah
LA = 21.422508 #Lintang Mekkah dalam Desimal
Cos_LA = cos(radians (LA)) #Cos Lintang Mekkah
Sin_LA = sin(radians (LA)) #Sin Lintang Mekkah
Tan_LA = Sin_LA / Cos_LA

#Bujur Mekkah
BA = 39.826192 # Bujur Mekkah dalam Desimal
Sin_BA = sin(radians (BA)) # Sin Bujur Mekkah
Cos_BA = cos(radians(BA)) # Cos Bujur Mekkah

#Menentukan Selisih Bujur Lokasi dan Kota Mekkah
BBA = (BB - BA) 
Sin_BBA = sin(radians (BBA))
Cos_BBA = cos(radians (BBA))

#Menentukan Tan B
X = Sin_BBA
Y = Cos_LB*Tan_LA
Z = Sin_LB*Cos_BBA

Tan_B = X / (Y - Z)
D_Tan_B = Tan_B
M_Tan_B = (D_Tan_B - int(D_Tan_B))*60.0
S_Tan_B = round((M_Tan_B - int(M_Tan_B))*60.0)
Tan_B1 = int(D_Tan_B), int(M_Tan_B), int(S_Tan_B)
print("Tan B (Desimal) = ", Tan_B)
print("Tan B (Sexagesimal) = ", Tan_B1)

#Menentukan B
B = degrees(atan(Tan_B))
print("Arc Tan B = ", B)
D_B = B
M_B = (D_B - int(D_B))*60.0
S_B = round((M_B - int(M_B))*60.0)
Bs = int(D_B), int(M_B), int(S_B)
print("Arc Tan B = ", Bs)

if LB<LA and BB>BA:
    kiblat = 360-B
    D_B = kiblat
    M_B = (D_B - int(D_B))*60.0
    S_B = round((M_B - int(M_B))*60.0)
    B1 = int(D_B), int(M_B), int(S_B)
    print("B (Kiblat Terhadap Utara) = ", B1)
    kiblat1 = 180 - B
    D_B1 = kiblat1
    M_B1 = (D_B1 - int(D_B1))*60.0
    S_B1 = round((M_B1 - int(M_B1))*60.0)
    B2 = int(D_B1), int(M_B1), int(S_B1)
    print("B (Kiblat Terhadap Selatan) = ", B2)

elif LB<LA and BB<BA:
    kiblat = -B
    D_B = kiblat
    M_B = (D_B - int(D_B))*60.0
    S_B = round((M_B - int(M_B))*60.0)
    B1 = int(D_B), int(M_B), int(S_B)
    print("B (Kiblat Terhadap Utara) = ", B1)
    kiblat1 = 180 - B
    D_B1 = kiblat1
    M_B1 = (D_B1 - int(D_B1))*60.0
    S_B1 = round((M_B1 - int(M_B1))*60.0)
    B2 = int(D_B1), int(M_B1), int(S_B1)
    print("B (Kiblat Terhadap Selatan) = ", B2)

elif LB>LA and BB<BA:
    kiblat = 180-B
    D_B = kiblat
    M_B = (D_B - int(D_B))*60.0
    S_B = round((M_B - int(M_B))*60.0)
    B1 = int(D_B), int(M_B), int(S_B)
    print("B (Kiblat Terhadap Utara) = ", B1)
    kiblat1 = 360 - B
    D_B1 = kiblat1
    M_B1 = (D_B1 - int(D_B1))*60.0
    S_B1 = round((M_B1 - int(M_B1))*60.0)
    B2 = int(D_B1), int(M_B1), int(S_B1)
    print("B (Kiblat Terhadap Selatan) = ", B2)

else:
    kiblat = 180 - B
    D_B = kiblat
    M_B = (D_B - int(D_B))*60.0
    S_B = round((M_B - int(M_B))*60.0)
    B1 = int(D_B), int(M_B), int(S_B)
    print("B (Kiblat Terhadap Utara) = ", B1)
    kiblat1 = -B
    D_B1 = kiblat1
    M_B1 = (D_B1 - int(D_B1))*60.0
    S_B1 = round((M_B1 - int(M_B1))*60.0)
    B2 = int(D_B1), int(M_B1), int(S_B1)
    print("B (Kiblat Terhadap Selatan) = ", B2)

print('++++=======================================++++')
