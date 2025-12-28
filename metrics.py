from datetime import datetime

def log_metric(metrics: list, metric_data: dict) -> dict:
    """[cite: 63] Kilo veya vücut ölçümü kaydeder."""
    metrics.append(metric_data)
    print("Ölçüm kaydedildi!")
    return metric_data

def goal_progress(users: list, metrics: list, user_id: str) -> dict:
    """[cite: 65] Kullanıcının hedefine ne kadar yaklaştığını hesaplar."""
    user = next((u for u in users if u['id'] == user_id), None)
    if not user or 'target_weight' not in user['goals']:
        return "Hedef kilo ayarlanmamış."

    # Kullanıcının son kilosunu bul
    user_metrics = [m for m in metrics if m['user_id'] == user_id and m['type'] == 'weight']
    if not user_metrics:
        return "Henüz kilo girişi yapılmamış."
    
    current_weight = float(user_metrics[-1]['value'])
    target_weight = float(user['goals']['target_weight'])
    diff = current_weight - target_weight
    
    status = f"Hedefe {abs(diff):.1f} kg kaldı."
    if diff > 0: status += " (Vermen gerek)"
    elif diff < 0: status += " (Alman gerek)"
    else: status = "Hedefine ulaştın!"
    
    return {"current": current_weight, "target": target_weight, "status": status}

def generate_ascii_chart(values: list):
    """[cite: 65] Basit bir metin tabanlı grafik çizer."""
    if not values: return ""
    print("\n--- İlerleme Grafiği ---")
    min_val = min(values)
    for v in values:
        bar = '#' * int(v - min_val + 1) # Basit ölçekleme
        print(f"{v} | {bar}")

def create_metric_input(user_id: str):
    print("\n--- Ölçüm Ekle ---")
    m_type = "weight" # Şimdilik sadece kilo
    value = float(input("Güncel Kilo (kg): "))
    date = datetime.now().strftime("%Y-%m-%d")
    return {
        "user_id": user_id,
        "type": m_type,
        "value": value,
        "date": date
    }
