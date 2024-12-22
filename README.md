# BMI Hesaplama Uygulaması

**Bu uygulama, kullanıcıların Boy-Kilo Endeksi'ni (BMI - Body Mass Index) kolayca hesaplamalarını sağlayan bir Python/Tkinter uygulamasıdır.** Kullanıcılar, boylarını ve kilolarını girerek BMI değerlerini öğrenebilir ve bu değerin hangi kategoriye girdiğini görebilir (ör. "Zayıf", "Normal", "Kilolu", "Obez").

---

## 🚀 Özellikler

- **Boy ve Kilo Girişi**: Kullanıcıdan boy (cm) ve kilo (kg) bilgilerini alır.
- **BMI Hesaplama**: Girilen değerlere göre BMI şu formülle hesaplanır:
  \[
  BMI = \frac{\text{Kilo (kg)}}{\text{Boy (m)}^2}
  \]
- **BMI Kategorileri**:
  - Zayıf: BMI < 18.5
  - Normal: 18.5 ≤ BMI < 24.9
  - Kilolu: 25 ≤ BMI < 29.9
  - Obez: BMI ≥ 30
- **Hata Yönetimi**: Geçersiz veya boş girişlerde kullanıcı dostu hata mesajları gösterilir.

---

## 📋 Gereksinimler

- Python 3.x
- Tkinter (standart olarak Python ile gelir, ek yükleme gerekmez)

---

## 🔧 Kurulum

1. **Projeyi klonlayın veya indirin**:
   ```bash
   git clone https://github.com/kullanici/bmi_calculator.git
   cd bmi_calculator
   ```

2. **Uygulamayı çalıştırın**:
   ```bash
   python bmi_calculator.py
   ```

---

## 📖 Kullanım

1. **Boyunuzu (cm) girin**.
2. **Kilonuzu (kg) girin**.
3. **Hesapla** butonuna tıklayın.
4. **Sonuç**: BMI değeri ve kategori ("Zayıf", "Normal", "Kilolu", "Obez") ekranda görüntülenir.

---

## 📝 Örnek Çalışma

- **Giriş**:
  - Boy: `175 cm`
  - Kilo: `70 kg`
- **Çıktı**:
  ```
  BMI: 22.86 - Normal
  ```

---

## ⚠️ Hata Yönetimi

- Geçersiz girişler: "Lütfen geçerli bir sayı girin!" mesajı gösterilir.
- Negatif veya sıfır değerler: "Boy ve kilo pozitif olmalıdır!" uyarısı verilir.

---

## 📌 Geliştirme Fikirleri

- BMI sonuçlarını kaydederek bir geçmiş tablosu oluşturma.
- Cinsiyet ve yaşa göre daha hassas kategoriler ekleme.
- Modern bir arayüz için Tkinter yerine PyQt veya Kivy kullanma.

---

## 📄 Lisans

Bu proje [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisanslanmıştır.

---

## 🤝 Katkıda Bulunma

Bu projeyi geliştirmek veya sorunları rapor etmek için pull request veya issue açabilirsiniz.
