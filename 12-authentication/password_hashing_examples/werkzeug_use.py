from werkzeug.security import generate_password_hash, check_password_hash

# Initialise password:
password = 'D4c-BzL-s11-q64'

# Hash the password:
hashed_password = generate_password_hash(password)
print(hashed_password)

# Check 'wrong password' vs hashed password:
check = check_password_hash(hashed_password, 'wrongpassword')
print(check)

# Check password vs hashed password:
check = check_password_hash(hashed_password, password)
print(check)
