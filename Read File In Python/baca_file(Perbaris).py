file_puisi = open("Read File In Python/puisi.txt", "r")
puisi = file_puisi.readlines()  # MEMBACA PERBARIS
print(puisi[0])  # MEMANGGIL BARIS 1
print(puisi[1])  # MEMANGGIL BARIS 2
file_puisi.close()


file_puisi = open("Read File In Python/puisi.txt", "r")
puisi = file_puisi.read()  # MEMBACA SELURUH BARIS
print(puisi)

file_puisi.close()
