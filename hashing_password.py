from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Функция для хеширования пароля
def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

# Функция для проверки пароля
def check_password(hashed_password, password):
    return bcrypt.check_password_hash(hashed_password, password)