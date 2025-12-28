import storage
import profiles
import workouts
import nutrition
import metrics
from datetime import datetime

def main():
    # 1. Tüm Verileri Yükle
    users, workout_list, meal_list, metric_list = storage.load_state("data")
    current_user = None

    while True:
        if not current_user:
            print("\n=== FITNESS TRACKER ===")
            print("1. Giriş Yap")
            print("2. Kayıt Ol")
            print("3. Çıkış")
            choice = input("Seçim: ")

            if choice == '1':
                email = input("Email: ")
                pin = input("PIN: ")
                user = profiles.authenticate_user(users, email, pin)
                if user:
                    current_user = user
                    print(f"\nHoşgeldin, {user['name']}!")
                else:
                    print("Hatalı giriş!")
            
            elif choice == '2':
                p_data = profiles.create_profile_input()
                if profiles.register_user(users, p_data):
                    print("Kayıt başarılı! Giriş yapınız.")
                    storage.save_state("data", users, workout_list, meal_list, metric_list)
            
            elif choice == '3':
                break
        else:
            # Giriş Yapmış Kullanıcı Menüsü
            print(f"\n--- MENÜ ({current_user['name']}) ---")
            print("1. Antrenman Ekle")
            print("2. Antrenman Özeti")
            print("3. Öğün Ekle (Nutrition)")
            print("4. Günlük Kalori Raporu")
            print("5. Kilo Gir (Metrics)")
            print("6. Hedef İlerlemesi ve Grafik")
            print("7. Yedek Al")
            print("8. Oturumu Kapat")
            
            choice = input("Seçim: ")

            if choice == '1':
                w_data = workouts.create_workout_input(current_user['id'])
                workouts.log_workout(workout_list, w_data)
            
            elif choice == '2':
                workouts.weekly_workout_summary(workout_list, current_user['id'])
            
            elif choice == '3': # Nutrition Ekleme
                m_data = nutrition.create_meal_input(current_user['id'])
                nutrition.log_meal(meal_list, m_data)

            elif choice == '4': # Kalori Raporu
                today = datetime.now().strftime("%Y-%m-%d")
                summary = nutrition.daily_calorie_summary(meal_list, current_user['id'], today)
                print(f"\nBugün ({summary['date']}) Toplam: {summary['total_calories']} kcal")
                for item in summary['items']:
                    print(f"- {item}")

            elif choice == '5': # Kilo Takibi
                met_data = metrics.create_metric_input(current_user['id'])
                metrics.log_metric(metric_list, met_data)

            elif choice == '6': # Grafik ve Hedef
                prog = metrics.goal_progress(users, metric_list, current_user['id'])
                print(f"\nDurum: {prog}")
                # Kullanıcının geçmiş kilolarını çekip grafik çizelim
                user_vals = [m['value'] for m in metric_list if m['user_id'] == current_user['id']]
                metrics.generate_ascii_chart(user_vals)

            elif choice == '7':
                storage.backup_state("data", "backups")
            
            elif choice == '8':
                current_user = None
                print("Çıkış yapıldı.")
            
            # Her işlemden sonra otomatik kaydet [cite: 9]
            storage.save_state("data", users, workout_list, meal_list, metric_list)

if __name__ == "__main__":
    main()
