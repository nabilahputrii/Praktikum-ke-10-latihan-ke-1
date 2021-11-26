# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 10:04:24 2021

@judul : Praktikum ke-10 latihan ke-1
@NIM : 065002100002
@author: Nabilah Putri

"""

def write(data):
    f = open("Biodata.txt", "w")
    f.write(data)
    f.close()
    
def read():
    h = open("Biodata.txt", 'r')

    line = h.readline()
    print(line)
    while line:
        line = h.readline()
        print(line)

    h.close()
        
print ("Masukan Biodata kamu")

nama = input("MASUKAN NAMA KAMU: ")
umur = input("MASUKAN UMUR KAMU: ")
alamat = input("MASUKAN ALAMAT KAMU: ")
email = input ("MASUKAN EMAIL KAMU:")
dosen = input ("MASUKAN DOSEN KAMU :")
data= "Nama: {}\nUmur: {}\nAlamat: {}\nEmail: {}\nDosen: {}\n".format(nama, umur, alamat, email, dosen)

print("=========================")
write(data)
print("berikut ini adalah data kamu")
read()