import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+"
password_length = 12
password = "".join(random.choice(characters) for i in range(password_length))
print(f"生成的密码是：{password}")