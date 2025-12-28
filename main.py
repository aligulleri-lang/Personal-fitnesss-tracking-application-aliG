import storage
import profiles
import workouts

def main():
    # 1. Verileri Yükle [cite: 28, 71]
    users, workout_list = storage.load_state("data")
    current_user = None

    while True:
        if not current_user:
            print("\n--- HOŞGELDİNİZ ---")
            print("1. Giriş Yap")
            print("2. Kayıt Ol")
            print("3. Çıkış")
            choice = input("Seçiminiz: ")

            if choice == '1':
                email = input("Email: ")
                pin = input("PIN: ")
                user = profiles.authenticate_user(users, email, pin) # [cite: 31]
                if user:
                    current_user = user
                    print(f"Hoşgeldin, {user['name']}!")
                else:
                    print("Hatalı giriş!")
            
            elif choice == '2':
                profile_data = profiles.create_profile_input()
                new_user = profiles.register_user(users, profile_data) # [cite: 30]
                if new_user:
                    print("Kayıt başarılı! Lütfen giriş yapın.")
                    storage.save_state("data", users, workout_list) # Kaydet [cite: 29]
            
            elif choice == '3':
                print("Çıkış yapılıyor...")
                break
        else:
            # Giriş yapmış kullanıcı menüsü [cite: 11]
            print(f"\n--- MENÜ ({current_user['name']}) ---")
            print("1. Antrenman Ekle")
            print("2. Antrenman Özeti Gör")
            print("3. Oturumu Kapat")
            choice = input("Seçiminiz: ")

            if choice == '1':
                w_data = workouts.create_workout_input(current_user['id'])
                workouts.log_workout(workout_list, w_data) # [cite: 39]
                storage.save_state("data", users, workout_list) # Her işlemden sonra kaydet
            
            elif choice == '2':
                workouts.weekly_workout_summary(workout_list, current_user['id']) # [cite: 44]
            
            elif choice == '3':
                current_user = None
                print("Oturum kapatıldı.")

if __name__ == "__main__":
    main()
