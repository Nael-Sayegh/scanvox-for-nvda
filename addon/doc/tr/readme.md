# NVDA için Scanvox

* Yazar: Nael Sayegh
* İletişim: [infos@nael-accessvision.com](mailto:infos@nael-accessvision.com)
* [Kararlı sürümü indirin][1];
* NVDA Uyumluluğu: 2021.3 ve sonrası;
* [GitHub'daki kaynak kodu][2];

# Sunum

Bu eklenti, basılı belgelerinizi okumak için Scanvox yazılımını kullanır. Yazılım geliştiricisinin yardımıyla oluşturulmuştur ve herhangi bir ek kurulum gerektirmez.

## Önkoşullar 

Bu eklentiyi kullanmak için bilgisayarınıza bağlı, çoğu tarayıcıda olduğu gibi TWAIN veya WIA uyumlu bir USB tarayıcınızın olması gerekir.

## Nasıl çalışır

Bu eklentiyi kullanmak için NVDA menüsü VE ardından Scanvox'u seçin.  
Bu iletişim kutusunda, Tara düğmesine tıklayarak bir tarama başlatabilirsiniz.  
Taramanın başlaması birkaç saniye sürer ve tarama işleminin sonunda taranan metin otomatik olarak yüksek sesle okunur.  
NVDA menüsü Ayarlar ve ardından NVDA için scanvox kategorisine giderek otomatik oynatmayı devre dışı bırakabilirsiniz.  
Tüm sayfalar taranana kadar bu düğmeye basın.  
Yeni taradığınız sayfayı silmek istiyorsanız, Sekme ile  taranan düğmesinin yanındaki “son taranan sayfayı sil” düğmesine basabilir veya alt+l kısayolunu kullanabilirsiniz.  
İşiniz bittiğinde, taranan düğmesinden shift+tab yaparak veya tüm sayfaların içeriğini içeren bir düzenleme alanına erişmek için alt+t yaparak taranan farklı sayfaları okuyabilirsiniz.  
Bu düzenleme alanında, sayfadan sayfaya hızlı bir şekilde geçmek istiyorsanız, önceki sayfa ve sonraki sayfa düğmelerini kullanabilir veya ctrl+shift+yukarı ok ve ctrl+shift+aşağı ok kısayollarını kullanabilirsiniz.  
İlgili düğmeleri kullanarak dosyayı kaydedebilir veya doğrudan Not Defteri'nde açabilirsiniz.  
Yeni bir belge taramak için taranan sayfaları silmek isterseniz, tüm taranan sayfaları iptal etmek için düğmesine basabilirsiniz.  
Scanvox'tan çıktığınızda, taranan tüm sayfalar silinir.  

### Klavye kısayolları

"Scanvox for NVDA" eklentisi, nvda+alt+s tuşlarına basılarak bilgisayarınızın herhangi bir yerinden başlatılabilir.  
Bu hareket, girdi hareketleri iletişim kutusunda değiştirilebilir.

## Değişiklikler

### Sürüm 2025.07.01

  * NVDA 2025.1 ile uyumluluk test edildi

### Sürüm 2024.08.15

  * Düzenleme alanında, bir sayfadan diğerine hızlıca geçmek için artık önceki ve sonraki sayfa tuşlarını veya ctrl+shift+yukarı ok ve ctrl+shift+aşağı ok tuşlarını kullanabilirsiniz.
  * Son taranan sayfayı silmek için düğme eklendi.
  * Dosya kaydetme iletişim kutusundaki Biçim listesindeki dosya biçimlerinin tersine çevrilmesi. Varsayılan biçim docx'tir.

### Sürüm 2024.07.02

  * Sil'e tıkladıktan sonra sayfa numaralarının artmaya devam etmesi sorunu düzeltildi.

### Sürüm 2024.06.01

  * Yeni özelliklerin test edilebilmesi ve Çevirmenler için bir Geliştirici kanalı eklendi.
  * Türkçe dil desteği eklendi.
  * Bir Word belgesini kaydederken, her sayfa dosyaya yeni bir sayfa olarak eklenir.
  * Scanvox'un yüklendiğini belirtmek için NVDA günlüğüne bir mesaj eklendi.
  * Yardım belgeleri güncellendi.

### Sürüm 2024.05.04

  * Güncelleme sistemi iyileştirildi.
  * Rusça çeviri güncellendi.
  * Fransızca çeviri düzeltmeleri.
  * Sil düğmesine basıldığında düzenleme alanının içeriğinin silinmemesine neden olan bir hata düzeltildi.
  * İmleç otomatik olarak düzenleme alanında taranan sayfanın başına yerleştirilir.
  * Düzenleme alanında taranan her sayfanın üstüne sayfa numarası eklenir.
  * Scanvox menüsü NVDA>Araçlar menüsünden, NVDA ana menüsüne taşındı.

### Version 2024.03.20

  * Çekçe çeviri eklendi.
  * Portekizce çeviri eklendi.
  * Tara düğmesinin önüne, yeni taranan metnin anında okunmasına olanak tanıyan bir düzenleme alanı eklendi.
  * Belgenin otomatik okunmasını devre dışı bırakmak / etkinleştirmek için bir parametre eklendi. NVDA menüsü ayarları ve ardından NVDA için Scanvox dalına gidin.
  * Rusça çeviri eklendi.

### Sürüm 2024.01.10

  * Sürümün yeni özelliklerine ilişkin yardımı açan "Yenilikler" düğmesini eklemek için sistem değişikliği güncellendi.
  * Taramadan sonra taranan sayfanın otomatik okunması eklendi.
  * Sayfanın ne zaman değiştiğini belirtmek için dosyaya bir sayfa ayırıcı (20 yıldız) eklendi.

### Sürüm 2024.01.03

  * Fransızca yardım dosyası güncellendi.

### Sürüm 2023.12.29

  * İlk sürüm.

[1]: https://github.com/Nael-Sayegh/scanvox-for-nvda/releases/download/2025.07.01/scanvox-2025.07.01.nvda-addon

[2]: https://github.com/Nael-Sayegh/scanvox-for-nvda