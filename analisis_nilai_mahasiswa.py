# Praktik: Analisis Nilai Mahasiswa

# Fungsi menghitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0

    return sum(data) / len(data)


# Fungsi menentukan nilai yang lulus
def nilai_lulus(data, batas=60):
    hasil = []

    for x in data:
        if x >= batas:
            hasil.append(x)

    return hasil


# Input: 10 nilai mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Proses pengolahan data
banyak_data = len(nilai)
total = sum(nilai)
rata = rata_rata(nilai)
minimum = min(nilai)
maksimum = max(nilai)

# Proses kelulusan
lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
belum_lulus = banyak_data - jumlah_lulus

# Output
print("===================================")
print("     ANALISIS NILAI MAHASISWA")
print("===================================")

print("Data nilai    :", nilai)
print("Banyak data   :", banyak_data)
print("Total nilai   :", total)
print(f"Rata-rata     : {rata:.2f}")
print("Nilai minimum :", minimum)
print("Nilai maksimum:", maksimum)

print("-----------------------------------")
print("HASIL KELULUSAN")
print("-----------------------------------")

print("Batas lulus   : 60")
print("Nilai lulus   :", lulus)
print("Jumlah lulus  :", jumlah_lulus)
print("Belum lulus   :", belum_lulus)

print("===================================")


# Test Case
print("\n=== PENGUJIAN PROGRAM ===")

# Test Case 1
data1 = [60, 70, 80]
print("Test Case 1:", data1)
print("Rata-rata:", rata_rata(data1))
print("Minimum:", min(data1))
print("Maksimum:", max(data1))
print("Jumlah lulus:", len(nilai_lulus(data1)))

# Test Case 2
data2 = [59, 60, 61]
print("\nTest Case 2:", data2)
print("Jumlah lulus:", len(nilai_lulus(data2)))

# Test Case 3
data3 = []
print("\nTest Case 3:", data3)
print("Rata-rata:", rata_rata(data3))