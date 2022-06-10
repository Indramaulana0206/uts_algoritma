def daftar_minuman():
    print('minuman \tharga ')
    print('1.sprite \tRp. 3500')
    print('2.Coca Cola\tRp. 3000')
    print('3.Adem sari\tRp. 5000')
    print('4.Indomilk\tRp. 4000')
    print('5.bear breand\tRp. 14.000')
def harga_minuman(nomer_minuman):
    switcher = {
        1 : 3500,
        2 : 3000,
        3 : 5000,
        4 : 4000,
        5 : 14000,
    }
    return switcher.get(nomer_minuman,'nomer yg anda masukkan tidak ada dalam daftar')
def cek_uang(uang):
    if uang < 5000:
        print('minimal uang yang dimasukkan harus Rp.5000')
        return False
    if uang % 5000 != 0:
        print('uang harus kelipatan RP.5000')
        return False
    return True
def uang_kembali(cekUang, uang, harga):
    if cekUang == True :
        kembalian = uang-harga
        print("kembalian anda sebesar Rp.", kembalian)

daftar_minuman()

no_minuman = int(input('pilih nomer minuman anda : '))
uang = int(input('masukkan uang anda = Rp.'))
cekUang = cek_uang(uang)
harga = harga_minuman(no_minuman)
uang_kembali(cekUang,uang,harga)



