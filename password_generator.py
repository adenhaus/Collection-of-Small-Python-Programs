import random

# Define acceptable characters
chars = "abcdefghijklmnopqrstuvwxyzAVCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()+=-<>,.[]{}?/"
chars_list = []

# Fill a list with these characters
for i in chars:
    chars_list.append(i)

password = ""

length = int(input("How long would you like the password to be? "))

# Choose random characters for password
for i in range(0, length):
    password = password + random.choice(chars_list)

# Print result
print(password)
