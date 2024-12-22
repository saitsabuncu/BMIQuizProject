import tkinter as tk


def calculate_bmi():
    """BMI hesaplama ve sonuçları ekrana yazma."""
    try:
        # Kullanıcı girdilerini al
        height = float(entry_height.get()) / 100  # cm'den metreye çevir
        weight = float(entry_weight.get())

        if height <= 0 or weight <= 0:
            label_error.config(text="Boy ve kilo pozitif olmalıdır!", fg="red")
            label_result.config(text="")  # Sonuç kısmını temizle
            return

        # BMI hesaplama
        bmi = weight / (height ** 2)

        # Kategoriyi belirleme
        if bmi < 18.5:
            category = "Zayıf"
            color = "blue"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
            color = "green"
        elif 25 <= bmi < 29.9:
            category = "Kilolu"
            color = "orange"
        else:
            category = "Obez"
            color = "red"

        # Hata mesajını temizle ve sonucu göster
        label_error.config(text="")
        label_result.config(text=f"BMI: {bmi:.2f} - {category}", fg=color)
    except ValueError:
        # Geçersiz girişlerde hata mesajını göster
        label_error.config(text="Lütfen geçerli bir sayı girin!", fg="red")
        label_result.config(text="")  # Sonuç kısmını temizle


# Ana pencere
root = tk.Tk()
root.title("BMI Hesaplama")
root.geometry("300x300")

# Boy girişi
label_height = tk.Label(root, text="Boy (cm):", font=("Arial", 12))
label_height.pack(pady=5)

entry_height = tk.Entry(root, font=("Arial", 12))
entry_height.pack(pady=5)

# Kilo girişi
label_weight = tk.Label(root, text="Kilo (kg):", font=("Arial", 12))
label_weight.pack(pady=5)

entry_weight = tk.Entry(root, font=("Arial", 12))
entry_weight.pack(pady=5)

# Hesapla butonu
button_calculate = tk.Button(root, text="Hesapla", font=("Arial", 12), command=calculate_bmi)
button_calculate.pack(pady=10)

# Hata mesajı etiketi
label_error = tk.Label(root, text="", font=("Arial", 10))
label_error.pack(pady=5)

# Sonuç etiketi
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=10)

# Pencereyi çalıştır
root.mainloop()
