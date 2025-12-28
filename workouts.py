from datetime import datetime

def log_workout(workouts: list, workout_data: dict) -> dict:
    """Yeni bir antrenman kaydeder[cite: 39]."""
    # Benzersiz ID oluştur
    workout_data['id'] = str(len(workouts) + 1)
    workouts.append(workout_data)
    print("Antrenman başarıyla kaydedildi!")
    return workout_data

def weekly_workout_summary(workouts: list, user_id: str):
    """Basit bir haftalık özet gösterir[cite: 37, 44]."""
    count = 0
    total_duration = 0
    for w in workouts:
        if w['user_id'] == user_id:
            count += 1
            total_duration += int(w['duration'])
    
    print(f"\n--- Özet ---")
    print(f"Toplam Antrenman Sayısı: {count}")
    print(f"Toplam Süre: {total_duration} dakika")

def create_workout_input(user_id: str):
    print("\n--- Antrenman Ekle ---")
    w_type = input("Tip (Strength/Cardio): ")
    duration = input("Süre (dk): ")
    date = datetime.now().strftime("%Y-%m-%d") # Otomatik bugün
    return {
        "user_id": user_id,
        "type": w_type,
        "duration": duration,
        "date": date,
        "exercises": [] # Detaylar eklenebilir
    }
