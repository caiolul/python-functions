import random


lower_case = "qwertyuiopasdfghjlçzxcvbnm"
upper_case = "QWERTYUIOPASDFGHJKLÇZXCVBNM"
number = "0123456789"
symbols = "{}[]!@$%¨&*()_+<>,.:;?|/"

all = lower_case+upper_case+number+symbols
length = 16
password = "".join(random.sample(all, length))
print(password)
