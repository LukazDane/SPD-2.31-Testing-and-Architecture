# By Kami Bigdely
# Split temp variable

def save_into_db(info):
    print("saved into databse")


username = input('Please enter your username: ')
save_into_db(username)
birthyear = int(input('Please enter your birth year: '))
age = 2020 - birthyear
print("You are", age, "years old.")
