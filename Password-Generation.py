import random
import string
def generate strong_password(lenght=8):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=random.choice(string.ascii_upercase)+random,choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
password_list=list(password) 
    random.shuffle(password_list) 
password +=''.join(password_list)
return password
   strong_password=strong_password=strong_password()
   print ("generated strong password:", strong_password)
