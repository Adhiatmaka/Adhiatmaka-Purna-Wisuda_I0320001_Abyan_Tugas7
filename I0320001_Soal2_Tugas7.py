judul = " PENGHITUNG IPK "
print(judul.center(70, '='))
n = int(input("Semester : "))
data = []
print()

i = 1
while i <= n:
    nilai = float(input("Masukkan IP ke-%d : " %i))
    data.append(nilai)
    i = i + 1
print()
print("Data IP : ", data)
print()

import math
print("IP terendah : ", min(data))
print()

import math
print("IP tertinggi : ", max(data))
print()

import math
rata_rata = sum(data) / n
print("IPK : ", rata_rata)
print()

import math
print("IPK dibulatkan ke atas : ", math.ceil(rata_rata))
print()

import math
print("IPK dibulatkan ke bawah : ", math.floor(rata_rata))