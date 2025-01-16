# Inputs
username = input("Enter your username: ")
is_alnum = username.isalnum()
length = len(username)
is_valid = False

# Nested If/Else

if username:
    if is_alnum:
        if length >= 6:
            if length <= 12:
                print("Username is valid.")
            else:
                print("Username is too long.")
        else:
            print("Username is too short.")
    else:
        print("Username must be alphanumeric.")
else:
    print("Username cannot be empty.")

# Fixed If/Else

if length >= 6 and length <= 12:
    print("Username is valid")
elif is_alnum:
    print("Username must be alphanumeric.")
elif length < 6:
    print("Username is too short.")
elif length > 12:
    print("Username is too long.")
else:
    print("Username cannot be empty.")
