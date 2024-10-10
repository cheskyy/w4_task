r, c, n = list(map(int, input().split()))
alas = [list(map(int, input().split())) for _ in range(r)]
langkah = input() #N

x, y = 0, 0
gold = alas[x][y]  # Emas di petak awal
alas[x][y] = 0  # Petak awal sudah diambil emasnya

for langka in langkah:
    if langka == 'L':
        if y - 1 >= 0:  # Cek apakah tidak keluar batas ke kiri
            y -= 1
            gold += alas[x][y] - 2  # Emas berkurang 2
        else:
            print("Gerakanmu salah bung!")
            exit()
    
    elif langka == 'R':
        if y + 1 < c:  # Cek apakah tidak keluar batas ke kanan
            y += 1
            gold += alas[x][y] + 3  # Emas bertambah 3
        else:
            print("Gerakanmu salah bung!")
            exit()

    elif langka == 'D':
        if x + 1 < r:  # Cek apakah tidak keluar batas ke bawah
            x += 1
            gold += alas[x][y] + 3  # Emas bertambah 3
        else:
            print("Gerakanmu salah bung!")
            exit()
    
    elif langka == 'U':
        if x - 1 >= 0:  # Cek apakah tidak keluar batas ke atas
            x -= 1
            gold += alas[x][y] - 2  # Emas berkurang 2
        else:
            print("Gerakanmu salah bung!")
            exit()
    
    # Set emas di petak saat ini ke 0 karena sudah diambil
    alas[x][y] = 0

# Output total emas yang dikumpulkan
print(gold)
