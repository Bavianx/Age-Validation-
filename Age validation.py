Bavian_Age = 19
Age_University = 18

if Bavian_Age > Age_University:
    print("Welcome to university!")
elif Bavian_Age == Age_University:
    print("You ARE a first year!")
else:
    print("YOURE NOT OLD ENOUGH!")


def print_bavian():
    text = "Bavian!!!!"
    print(text)
print_bavian()



import bcrypt

def login():
    #get username and password from user
    username = input("Enter username: ")
    password = input("Enter password: ")

    #check if username and password are valid
    if check_credentials(username, password):
        #if valid, show success message and allow access
        print("Access granted.")
    else:
        #if not valid, show error message and deny access
        print("Access denied. Incorrect username or password.")

def check_credentials(username, password):
    # check if username and password match a valid account
    try:
        valid_accounts = {
            "username1": "$2b$12$iJjyYnkq1q3MhN/X9vU6xOrU6E2Z8GwW0g/vj.Dd3Fq3/5C5X5J5G",
            "username2": "$2b$12$iJjyYnkq1q3MhN/X9vU6xOrU6E2Z8GwW0g/vj.Dd3Fq3/5C5X5J5G"
        }
        hashed_password = valid_accounts[username]
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            return True
        else:
            return False
    except KeyError:
        # If the username is not in the dictionary
        return False

#run the login function
login()