def register_user(users: list, profile: dict) -> dict:
    """Yeni bir kullanıcı profili oluşturur."""
    users.append(profile)
    return profile

def authenticate_user(users: list, email: str, pin: str) -> dict | None:
    """Giriş bilgilerini doğrular."""
    for user in users:
        if user['email'] == email and user['pin'] == pin:
            return user
    return None
