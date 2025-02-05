from passlib.context import CryptContext

# Initialize CryptContext with bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash the password
hashed_password = pwd_context.hash("nassif123")

# Print the hashed password
print(hashed_password)
