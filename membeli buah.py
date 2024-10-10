N,K = map(int, input("masukkan jumlah buah (N) dan jumlah lembar uang (K)").split())
harga_buah = list(map(int, input("masukkan harga buah(A) :").split()))
banyak_buah_yang_bisa_dibeli = []
for i in harga_buah:
    if i <= K:
        banyak_buah_yang_bisa_dibeli.append(i)
print(len(banyak_buah_yang_bisa_dibeli))
"""
menghitung banyaknya char dalam satu var
"""