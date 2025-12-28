import os
import json

def kurulum_yap():
    # 1. data klasörünü oluştur
    if not os.path.exists('data'):
        try:
            os.makedirs('data')
            print("✅ 'data' klasörü başarıyla oluşturuldu.")
        except Exception as e:
            print(f"❌ Klasör oluşturulurken hata çıktı: {e}")
            return
    else:
        print("ℹ️ 'data' klasörü zaten varmış.")

    # 2. Gerekli dosyaları oluştur
    dosyalar = ['users.json', 'workouts.json', 'nutrition.json', 'metrics.json']
    
    for dosya_ismi in dosyalar:
        dosya_yolu = os.path.join('data', dosya_ismi)
        if not os.path.exists(dosya_yolu):
            try:
                with open(dosya_yolu, 'w') as f:
                    json.dump([], f) # İçine boş liste [] koyar
                print(f"✅ {dosya_ismi} oluşturuldu.")
            except Exception as e:
                print(f"❌ {dosya_ismi} oluşturulamadı: {e}")
        else:
            print(f"ℹ️ {dosya_ismi} zaten var.")

    print("\n🎉 Kurulum Tamamlandı! Artık 'python main.py' diyerek projeyi çalıştırabilirsin.")

if __name__ == "__main__":
    kurulum_yap()
