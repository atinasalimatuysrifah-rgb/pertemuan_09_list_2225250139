# Latihan 5: Filter Kelulusan

# Input
nilai = [75, 55, 80, 60, 45, 90]

# Batas kelulusan
batas = 60

# Menyimpan nilai yang lulus
lulus = []

# Proses
for x in nilai:
    if x >= batas:
        lulus.append(x)

# Output
print("=== FILTER KELULUSAN ===")
print("Data nilai:", nilai)
print("Batas kelulusan:", batas)
print("Nilai lulus:", lulus)
print("Jumlah lulus:", len(lulus))