def hitung_biaya_parkir(jenis_kendaraan, lama_parkir):
    # Tarif awal dan tambahan
    if jenis_kendaraan == "motor":
        tarif_awal = 1000
        tarif_per_jam = 500
    elif jenis_kendaraan == "mobil":
        tarif_awal = 1500
        tarif_per_jam = 1000
    else:
        return "Jenis kendaraan tidak valid"
    
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
jenis = input("Masukkan jenis kendaraan (motor/mobil): ").lower()
lama = float(input("Masukkan lama parkir (jam): "))

# Hitung biaya
biaya = hitung_biaya_parkir(jenis, lama)
print(f"Biaya parkir adalah Rp {biaya}")