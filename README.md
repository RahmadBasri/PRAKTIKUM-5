#PENJELASAN PROGRAM

#MEMBUAT VARIABEL YANG BERISI= Tambah, Ubah, Hapus, Lihat, Cari, Keluar

*Bila user menginputkan T / Tambah maka akan di suruh mengisi tambah data mahasiswa di dalam   tambah data mahasiswa terdiri dari nama, nim, tugas, uts, uas.

*Bila user menginputkan U / Ubah data mahasiswa maka akan ke form mengubah data mahasiswa,dan di sana memakai Dictionary Keys untuk mengambil seluruh kuncinya, dan Bila user memasukkan yang tidak ada data mahasiswanya maka akan keluar Alert Daftar nilai mahasiswa (0) / / tidak ada

*Bila User menginputkan H / Hapus data mahasiswa maka akan ke form hapus data mahasiswa, dan di sana memakai keyword del untuk menghapus data mahasiswa, dan bila user memasukkan yang tidak ada data mahasiswanya maka akan keluar Alert Daftar (0) Tidak ada

*Bila user menginputkan L / Lihat Data mahasiswa maka akan ke Tampilan data mahasiswa dalam bentuk keseluruhan tabel data mahasiswa, dengan keyword items untuk mengambil key dan values nya.

*Bila user menginputkan C / Cari Data mahasiswa maka akan ke Tampilan data mahasiswa dalam bentuk satuan, hanya yang di inputkan user maka itulah yang akan tampil di tabel data mahasiswa,dan bila tidak sesuai dengan data mahasiswa maka akan muncul Alert Kontak (0) tidak ada

*Bila User Menginputkan K / Keluar maka akan Keluar dari Sistem
 

  #Dan Bila User Menginputkan Selain dari Tambah,Ubah,Hapus,Lihat,Cari,Keluar maka akan muncul alert Pilihan Menu Tidak Tersedia.


#FLOWCHART

![FLOWCHART PRAKTIKUM 5](https://user-images.githubusercontent.com/57025005/70366596-01739080-18cb-11ea-8344-4978614ddb78.jpg)

#HASIL

![contoh output'](https://user-images.githubusercontent.com/57025005/70366707-e48b8d00-18cb-11ea-9986-0522514269da.PNG)

==================================================================================================================================
RAHMAD={}
while True:
    print(" ")
    c = input("L)ihat, T)ambah, U)bah, H)apus, C)ari, K)eluar : ")
    if c.lower() == 'k':
        break

    elif c.lower() == 't':
        print("======TAMBAH DATA======")
        nama=input('Nama                 :')
        nim=input('NIM                   :')
        tugas=float(input('masukan nilai tugas :'))
        uts=float(input('masukkan nilai uts :'))
        uas=float(input('masukkan nilai uas :'))
        akhir= (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        RAHMAD[nama] = nim, tugas, uts, uas, akhir

    elif c.lower() == 'h':
        print('======HAPUS DATA MAHASISWA=======')
        nama=input("nama : ")
        if nama in data.keys():
            del data[nama]
    elif c.lower() == 'c' :
        print("cari RAHMAD")
        nama= input("Nama : ")
        if nama in RAHMAD.keys():
            print("data {0} adalah {1}"\
                  .format(nama, RAHMAD[nama]))

    elif c.lower() == 'l':
        print("=============================================================")
        print("| NO |   NAMA    |      NIM            |TUGAS| UTS | UAS | AKHIR |")
        print("=============================================================")
        i = 0
        for x in RAHMAD.items():
            i+=1
        print("| {6:2} | {0:12s} | {1:9s} | {2:3} | {3:3} | {4:4} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))

        print("===========================================================================================================================")

    elif c.lower() =='u' :
        print("Ubah RAHMAD")
        nama = input("Nama: ")
        if nama in RAHMAD.keys():
            nama=input("Nama: ")
            nim=input('NIM :')
            tugas=float(input('masukan nilai tugas :'))
            uts=float(input('masukkan nilai uts :'))
            uas=float(input('masukkan nilai uas :'))
            akhir= (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            RAHMAD[nama] = nim, tugas, uts, uas, akhir

        else:

            print("====================TIDAK ADA DATA==========================")

    elif c.lower() == 'c':
        print('===cari data mahasiswa==')
        nama=input('masukan Nama : ')
        if nama in RAHMAD.keys():
            print("Datanya", nama,"adalah {0}".format( RAHMAD[nama]))

        else:
            print("======================TIDAK ADA DATA========================")
