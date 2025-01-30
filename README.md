# BMIQuizProject

**BMIQuizProject**, kullanıcının Vücut Kitle İndeksi'ni (BMI) hesaplayan ve ardından BMI sonuçlarına göre bir dizi soruyla kullanıcıyı yönlendiren bir uygulamadır. Bu proje, sağlıklı yaşam farkındalığını artırmayı ve kullanıcıların kendi sağlık durumları hakkında bilgi sahibi olmalarını sağlamayı amaçlamaktadır.

## Özellikler

- **BMI Hesaplama:** Kullanıcının boy ve kilo bilgilerini alarak BMI değerini hesaplar.
- **Kişiselleştirilmiş Sorular:** Hesaplanan BMI değerine göre kullanıcılara özel sorular sunar.
- **Sonuç Analizi:** Kullanıcının verdiği cevaplara göre genel bir sağlık değerlendirmesi sağlar.

## Kurulum

1. **Depoyu Klonlayın:**

   ```bash
   git clone https://github.com/saitsabuncu/BMIQuizProject.git
   cd BMIQuizProject
   ```

2. **Sanal Ortam Oluşturun:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Gerekli Bağımlılıkları Yükleyin:**

   ```bash
   pip install -r requirements.txt
   ```

   *Not:* Eğer `requirements.txt` dosyası mevcut değilse, projenin kullandığı kütüphaneleri manuel olarak yüklemeniz gerekebilir.

## Kullanım

1. **Uygulamayı Başlatın:**

   ```bash
   python main.py
   ```

2. **Kullanıcı Arayüzü:**

   - Uygulama başlatıldığında, kullanıcıdan boy ve kilo bilgileri istenir.
   - BMI hesaplandıktan sonra, kullanıcıya bir dizi soru yöneltilir.
   - Tüm sorular cevaplandıktan sonra, genel bir sağlık değerlendirmesi sunulur.

## Katkı Sağlama

Katkılarınızı memnuniyetle karşılıyoruz! Projeye katkıda bulunmak için aşağıdaki adımları izleyebilirsiniz:

1. **Depoyu Fork'layın**
2. **Yeni Bir Branch Oluşturun:** `git checkout -b yeni-ozellik`
3. **Değişikliklerinizi Commit Edin:** `git commit -m 'Yeni özellik eklendi'`
4. **Branch'inizi Push Edin:** `git push origin yeni-ozellik`
5. **Pull Request Oluşturun`

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.

## İletişim

Herhangi bir sorunuz veya öneriniz varsa, lütfen [saitsabuncu](https://github.com/saitsabuncu) ile iletişime geçin.

---
