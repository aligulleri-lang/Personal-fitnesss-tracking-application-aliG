def register_user(users: list, profile: dict) -> dict:
    """Yeni bir kullanıcı oluşturur[cite: 30]."""
    # Basit bir ID atama ve e-posta kontrolü
    for user in users:
        if user['email'] == profile['email']:
            print("Bu email zaten kayıtlı.")
            return None
    
    profile['id'] = str(len(users) + 1)
    users.append(profile)
    return profile

def authenticate_user(users: list, email: str, pin: str) -> dict | None:
    """Email ve PIN ile giriş yapar[cite: 31]."""
    for user in users:
        if user['email'] == email and user['pin'] == pin:
            return user
    return None

def create_profile_input():
    print("\n--- Yeni Kullanıcı Kaydı ---")
    email = input("Email: ")
    pin = input("PIN (Şifre): ")
    name = input("İsim: ")
    age = int(input("Yaş: "))
    return {
        "email": email, "pin": pin, "name": name, 
        "age": age, "goals": {}
    }
        "email": email, "pin": pin, "name": name, 
        "age": age, "goals": {}
    }
