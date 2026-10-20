# Latihan 3: Manipulasi List

# Input
nilai = [75, 80, 65]

print("=== MANIPULASI LIST ===")
print("Data awal:", nilai)

# Mengubah nilai
nilai[1] = 82
print("Setelah diubah:", nilai)

# Menambahkan nilai
nilai.append(90)
print("Setelah ditambah:", nilai)

# Menyisipkan nilai
nilai.insert(1, 70)
print("Setelah disisipkan:", nilai)

# Menghapus nilai
nilai.remove(65)
print("Setelah dihapus:", nilai)

# Output akhir
print("Data akhir:", nilai)