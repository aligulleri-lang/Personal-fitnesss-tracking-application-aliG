import json
import os
import shutil
from datetime import datetime

# Veri kalıcılığı ve yedekleme işlemleri
def load_state(base_dir: str):
    """Tüm veri setlerini yükler."""
    users = _load_json(os.path.join(base_dir, "users.json"))
    workouts = _load_json(os.path.join(base_dir, "workouts.json"))
    meals = _load_json(os.path.join(base_dir, "nutrition.json")) # Yeni eklendi
    metrics = _load_json(os.path.join(base_dir, "metrics.json"))   # Yeni eklendi
    return users, workouts, meals, metrics

def save_state(base_dir: str, users: list, workouts: list, meals: list, metrics: list):
    """Tüm veri setlerini kaydeder."""
    _save_json(os.path.join(base_dir, "users.json"), users)
    _save_json(os.path.join(base_dir, "workouts.json"), workouts)
    _save_json(os.path.join(base_dir, "nutrition.json"), meals)   # Yeni eklendi
    _save_json(os.path.join(base_dir, "metrics.json"), metrics)    # Yeni eklendi

def backup_state(base_dir: str, backup_dir: str):
    """ Yedekleme işlemi."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copytree(base_dir, os.path.join(backup_dir, f"backup_{timestamp}"), dirs_exist_ok=True)
    print(f"Sistem yedeği alındı: backup_{timestamp}")

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
