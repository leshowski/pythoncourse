SECURE = (('L','#$'),('u','!'),('i','&'),('s','|<'))

def passwordsecure(password):
    for a,b in SECURE:
        password = password.replace(a,b)

    return password

password = input("Please provide your password here:")

print(f"your new password is {passwordsecure(password)}")