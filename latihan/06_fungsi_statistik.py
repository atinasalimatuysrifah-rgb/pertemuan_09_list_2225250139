# Latihan 6: Fungsi Statistik

# Fungsi menghitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0

    return sum(data) / len(data)


# Input
nilai = [75, 80, 65, 90, 88]

# Proses
hasil = rata_rata(nilai)

# Output
print("=== FUNGSI STATISTIK ===")
print("Data nilai:", nilai)
print(f"Rata-rata: {hasil:.2f}")

# Pengujian list kosong
print("Rata-rata list kosong:", rata_rata([]))