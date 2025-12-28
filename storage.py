import json
import os
import shutil
from datetime import datetime

DATA_DIR = "data"
BACKUP_DIR = "backups"

def load_state(base_dir: str):
    """Verilen klasörden kullanıcı ve antrenman verilerini yükler[cite: 71]."""
    users = _load_json(os.path.join(base_dir, "users.json"))
    workouts = _load_json(os.path.join(base_dir, "workouts.json"))
    # Nutrition ve Metrics de buraya eklenebilir
    return users, workouts

def save_state(base_dir: str, users: list, workouts: list):
    """Tüm verileri JSON dosyalarına kaydeder[cite: 71]."""
    _save_json(os.path.join(base_dir, "users.json"), users)
    _save_json(os.path.join(base_dir, "workouts.json"), workouts)

def backup_state(base_dir: str, backup_dir: str):
    """Verilerin yedeğini alır[cite: 68, 72]."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copytree(base_dir, os.path.join(backup_dir, f"backup_{timestamp}"), dirs_exist_ok=True)
    print(f"Yedek alındı: {timestamp}")

def _load_json(filepath: str) -> list:
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def _save_json(filepath: str, data: list):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
