def hitung_biaya_parkir_terminal(lama_parkir):
    # Tarif dasar
    tarif_awal = 3000
    tarif_per_jam = 1500
    
    # Hitung biaya parkir
    if lama_parkir <= 2:
        biaya_total = tarif_awal
    else:
        biaya_total = tarif_awal + (lama_parkir - 2) * tarif_per_jam
    
    # Tambahan biaya jika lebih dari 24 jam
    if lama_parkir > 24:
        biaya_total += 10000
    
    return biaya_total

# Input
lama = float(input("Masukkan lama parkir (jam): "))

# Hitung biaya
biaya = hitung_biaya_parkir_terminal(lama)
print(f"Biaya parkir adalah Rp {biaya}")