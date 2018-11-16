from bcrypt import hashpw, checkpw, gensalt

# Initialise password:
password = 'D4c-BzL-s11-q64'

# Hash the password:
hashed_password = hashpw(password, gensalt(10))
print(hashed_password)

# Check 'wrong password' vs hashed password:
check = checkpw('wrongpassword', hashed_password)
print(check)

# Check password vs hashed password:
check = checkpw(password, hashed_password)
print(check)
