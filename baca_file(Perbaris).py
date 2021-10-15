file_puisi = open("Read File In Python/puisi.txt", "r")
puisi = file_puisi.readlines()  # MEMBACA PERBARIS (outputnya jadi tuple string)
print(puisi[0])  # MEMANGGIL BARIS 1
print(puisi[1])  # MEMANGGIL BARIS 2
file_puisi.close()
