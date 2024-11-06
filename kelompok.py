import random

# Daftar siswa
siswa = ['Adinda', 'Ahmad Rifaldy', 'Alifa', 'Ananda', 'Andika C', 'Andromeda', 'Aryasatya', 'Azaoharoturraehana', 'Bellataria', 'Cindy', 'Davit', 'Dwi',
         'Firman', 'Indah', 'Inggil', 'Irfan', 'Irna', 'M.Raihan','M Rizky','M Andika', 'Najwa', 'Nanda', 'Nasywa','Nazrul','Nazwa', 'Patmawati',
         'Puspamurti','Putri Nur', 'Putri W', 'Raihan', 'Ranie', 'Riris','Sello','Siti','Theresia', 'Umar', 'Zahra']

# Jumlah kelompok yang diinginkan
jumlah_kelompok = 12

# Acak daftar siswa
random.shuffle(siswa)

# Bagi siswa menjadi kelompok
kelompok = [siswa[i::jumlah_kelompok] for i in range(jumlah_kelompok)]

# Cetak hasil pembagian kelompok
for i, k in enumerate(kelompok, 1):
    print(f"Kelompok {i}: {', '.join(k)}")