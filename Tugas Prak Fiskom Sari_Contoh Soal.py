# Sebuah motor kecil digunakan untuk memberi daya pada sebuah lift yang menaikkan beban beton dengan berat 750 N sampai ketinggian 15 m dalam 20 s.
# Berapakah daya minimum yang harus disediakan motor tersebut ?

# Menentukan variabel
F = 750  # Gaya dalam newton
h = 15   # Ketinggian dalam meter
t = 20   # Waktu dalam detik

# Menghitung Kecepatan Motor
v = h / t

# Menghitung kerja yang dilakukan
W = F * h

# Menghitung daya
P = W / t

print("Daya minimum yang harus disediakan oleh motor:", P, "Watt")
