BMI Hesaplama Uygulaması
Bu uygulama, kullanıcıların Boy-Kilo Endeksi'ni (BMI - Body Mass Index) kolayca hesaplamalarını sağlayan basit bir Python/Tkinter uygulamasıdır. Kullanıcı, boyunu ve kilosunu girdikten sonra BMI değeri ve kategorisi ("Zayıf", "Normal", "Kilolu", "Obez") ekranda gösterilir.

Özellikler
Boy ve kilo giriş alanları: Kullanıcıdan boy (cm) ve kilo (kg) bilgilerini alır.
BMI hesaplama: Girilen değerlere göre BMI formülü uygulanır:
BMI
=
Kilo
Boy
2
BMI= 
Boy 
2
 
Kilo
​
 
(Boy metre cinsinden alınır.)
BMI kategorileri:
Zayıf: BMI < 18.5
Normal: 18.5 ≤ BMI < 24.9
Kilolu: 25 ≤ BMI < 29.9
Obez: BMI ≥ 30
Kullanıcı geri bildirimleri: Geçersiz girişlerde veya hatalı değerlerde kullanıcı dostu hata mesajları gösterilir.
Kullanım
1. Gerekli Kütüphaneler
Uygulama yalnızca standart Python kütüphanelerini (Tkinter) kullanır. Ekstra bir yükleme gerekmez. Python'un 3.x sürümünün yüklü olduğundan emin olun.

2. Çalıştırma
Uygulama dosyasını indirin veya kopyalayın (ör. bmi_calculator.py).
Aşağıdaki komutla uygulamayı başlatın:
bash
Kodu kopyala
python bmi_calculator.py
3. Kullanım Adımları
Boy alanına (cm cinsinden) değer girin.
Kilo alanına (kg cinsinden) değer girin.
Hesapla butonuna tıklayın.
BMI sonucu ve kategorisi (ör. "Normal", "Obez") ekranda görüntülenecektir.
4. Örnek Çalışma
Boy: 175 cm
Kilo: 70 kg
Sonuç: BMI: 22.86 - Normal
Hata Yönetimi
Geçersiz giriş: Eğer sayı dışı bir değer girilirse, uygulama "Lütfen geçerli bir sayı girin!" şeklinde bir hata mesajı gösterir.
Negatif veya sıfır değerler: Boy veya kilo sıfırdan küçükse ya da sıfırsa, "Boy ve kilo pozitif olmalıdır!" uyarısı görüntülenir.
Proje Yapısı
calculate_bmi() Fonksiyonu:
Kullanıcı girişlerini alır.
BMI hesaplar ve kategoriyi belirler.
Hata durumlarını yönetir.
Tkinter UI:
Kullanıcıdan giriş alacak alanlar.
Hesapla butonu.
Hata ve sonuç etiketleri.
Katkıda Bulunma
Herhangi bir öneriniz veya iyileştirme fikriniz varsa, pull request veya issue açarak katkıda bulunabilirsiniz.

Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.
