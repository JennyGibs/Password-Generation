import random
import string
def generate_strong_password(length=4):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
  
  password += ''.join(random.choice(characters) for _ in range(length - 4))   
  password_list = list(password)
  random.shuffle(password_list)
  password = ''.join(password_list) 
  
  return password

strong_password = generate_strong_password()
print("Generated Strong Password:", strong_password)
