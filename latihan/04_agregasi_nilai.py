# Latihan 4: Agregasi Nilai

# Input
nilai = [75, 80, 65, 90, 88]

# Proses
total = sum(nilai)
banyak = len(nilai)
rata_rata = total / banyak
minimum = min(nilai)
maksimum = max(nilai)

# Output
print("=== AGREGASI NILAI ===")
print("Data nilai:", nilai)
print("Total:", total)
print(f"Rata-rata: {rata_rata:.2f}")
print("Minimum:", minimum)
print("Maksimum:", maksimum)