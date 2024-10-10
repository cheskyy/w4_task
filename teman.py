N, r, c = map(int, input("Masukkan jumlah siswa (N), jumlah baris (r), dan jumlah kolom (c): ").split())
kelas = [[0] * c for _ in range(r)]
posisi = {}

for _ in range(N):
    x, a, b = map(int, input(f"Masukkan nomor siswa x, baris a, dan kolom b (untuk siswa {_+1}): ").split())
    kelas[a - 1][b - 1] = x
    posisi[x] = (a - 1, b - 1)

for i in range(1, N + 1):
    a, b = posisi[i]
    tetangga = (kelas[a][b - 1] if b - 1 >= 0 else 0) or (kelas[a][b + 1] if b + 1 < c else 0)
    print(f"Siswa nomor {i} duduk bersebelahan dengan: {tetangga}")