N,M = map(int, input("masukkan jumlah barang (N) masukkan jumlah jumlah lembar uang (M) ").split()) 
P= list(map(int, input().split()))
C= list(map(int, input().split()))
max_price= 0
min_price= 0
"""
menggunakan max min price 
agar terhitung oleh yang di bawah
"""
for i in P:
    if i > 0:
        max_price += i
for j in C:
    if j < 1:
        min_price += j
hutang = (max_price-min_price)*-1
print (hutang)

"""
Kasus ini menggambarkan situasi di mana Bu Chanek berusaha melakukan belanja 
sambil mempertimbangkan batasan anggaran yang ditetapkan oleh suaminya, Pak Chanek. 
Dengan skenario ini, fokusnya adalah pada analisis nilai negatif 
dari barang dan bagaimana cara untuk memaksimalkan atau meminimalkan utang dalam pengeluaran belanja, 
yang juga menunjukkan elemen perhitungan dan strategi keuangan dalam pengelolaan uang.
"""