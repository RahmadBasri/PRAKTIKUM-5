RAHMAD={}
while True:
    print(" ")
    c = input("L)ihat, T)ambah, U)bah, H)apus, C)ari, K)eluar : ")
    if c.lower() == 'k':
        break

    elif c.lower() == 't':
        print("======TAMBAH DATA======")
        nama=input('Nama               :')
        nim=input('NIM                 :')
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
