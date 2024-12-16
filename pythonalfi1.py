def hitung_biaya(dimensi, berat):
    # Dimensi paket: panjang, lebar, tinggi
    panjang, lebar, tinggi = dimensi
    biaya_per_kg = 5000
    biaya_tambahan_dimensi = 0
    
    # Cek ukuran paket
    if panjang > 50 or lebar > 50 or tinggi > 50:
        biaya_per_kg = 7000
        biaya_tambahan_dimensi = 20000
    
    # Berat minimal 1 kg
    berat = max(berat, 1)
    
    # Hitung total biaya
    biaya_total = (biaya_per_kg * berat) + biaya_tambahan_dimensi
    return biaya_total

# Input
panjang = float(input("Masukkan panjang paket (cm): "))
lebar = float(input("Masukkan lebar paket (cm): "))
tinggi = float(input("Masukkan tinggi paket (cm): "))
berat = float(input("Masukkan berat paket (kg): "))

# Hitung biaya
biaya = hitung_biaya((panjang, lebar, tinggi), berat)
print(f"Biaya pengiriman adalah Rp {biaya}")