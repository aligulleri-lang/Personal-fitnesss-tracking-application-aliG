from datetime import datetime

def log_meal(meals: list, meal_data: dict) -> dict:
    """[cite: 52] Yeni bir öğün kaydeder."""
    meal_data['id'] = str(len(meals) + 1)
    meals.append(meal_data)
    print("Öğün başarıyla kaydedildi!")
    return meal_data

def daily_calorie_summary(meals: list, user_id: str, date: str) -> dict:
    """[cite: 55] Belirli bir gün için kalori özeti çıkarır."""
    total_cals = 0
    items = []
    
    for m in meals:
        if m['user_id'] == user_id and m['date'] == date:
            total_cals += int(m['calories'])
            items.append(f"{m['food_item']} ({m['calories']} kcal)")
    
    return {
        "date": date,
        "total_calories": total_cals,
        "items": items
    }

def create_meal_input(user_id: str):
    print("\n--- Öğün Ekle ---")
    food = input("Yiyecek Adı: ")
    calories = input("Kalori: ")
    date = datetime.now().strftime("%Y-%m-%d")
    return {
        "user_id": user_id,
        "food_item": food,
        "calories": calories,
        "date": date,
        "timestamp": datetime.now().strftime("%H:%M")
    }
