import os
import time
os.system("cls")

print("""
Hoşgeldin.

=======================================
[1] Toplama
[2] Çıkarma
[3] Çarpma
[4] Üssünü Alma
[5] Bölme
=======================================
	""")

veri = input("İşlem: ")

if veri =="1":
	x = input("İlk Sayı:")
	x = float(x)
	y = input("İkinci Sayı:")
	y = float(y)
	print("Sonuç: " , x + y)
	print("Program 5 Saniye Sonra Kapanacak.")



elif veri =="2":
	x = input("İlk Sayı:")
	x = float(x)
	y = input("İkinci Sayı:")
	y = float(y)
	print("Sonuç: ",x - y)
	print("Program 5 Saniye Sonra Kapanacak.")





elif veri =="3":
	x = input("İlk Sayı:")
	x = float(x)
	y = input("İkinci Sayı:")
	y = float(y)
	print("Sonuç: ",x * y)
	print("Program 5 Saniye Sonra Kapanacak.")





elif veri =="4":
	x = input("İlk Sayı:")
	x = float(x)
	y = input("İkinci Sayı:")
	y = float(y)
	print("Sonuç: ",x ** y)
	print("Program 5 Saniye Sonra Kapanacak.")




elif veri =="5":
	x = input("İlk Sayı:")
	x = float(x)
	y = input("İkinci Sayı:")
	y = float(y)
	print("Sonuç: ",x / y)
	print("Program 5 Saniye Sonra Kapanacak.")



else:
	print("Yanlış Bir Seçim Yaptınız.")
	print("Lütfen Düzgün Bir Seçim Yapınız.")
	print("Program Kapanıyor")
	quit()

time.sleep(5)