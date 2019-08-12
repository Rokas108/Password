"""This is where I store functions"""

def login(password_dict):
    username = input("Enter your username:")
    password = input("Enter your password:")
    if username in password_dict.keys():
        if password == password_dict.get(username, 'No point value assigned.'):
            print("\nyou have succesfully logged in")
        else:
            print("\nyour password is incorrect")
    else:
        print("\nThe username you have entered is not in the database, please sign up first")

def sign_up(password_dict):
    #in theory we would have to prevent overwriting keys (usernames) with new passwords
    username = input("Enter your username:")
    password = input("Enter your password:")
    password_dict[username] = password
    print("\nYour username and password have been stored, please remember them")