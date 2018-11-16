import bcrypt

# Initialise password:
password = 'D4c-BzL-s11-q64'

# Hash the password:
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(10))
print(hashed_password)

# Check 'wrong password' vs hashed password:
check = bcrypt.checkpw('wrongpassword', hashed_password)
print(check)

# Check password vs hashed password:
check = bcrypt.checkpw(password, hashed_password)
print(check)
