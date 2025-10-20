import random
import string
import time

class EmailPasswordGenerator:
    def generate(self):
        # Генерируем действительно уникальную почту
        timestamp = int(time.time())
        random_digits = ''.join(random.choices(string.digits, k=3))
        email = f"test_user_{timestamp}_{random_digits}@gmail.com"
        
        # Генерируем валидный пароль (минимум 6 символов)
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        
        return email, password
    